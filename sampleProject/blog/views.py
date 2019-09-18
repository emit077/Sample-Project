from django.shortcuts import render
from django.http import HttpResponse
from .models import user, blog_data
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def Registration(request):
    userentry = user()
    if request.method == 'GET':
        userentry.name = request.GET['name']
        userentry.mobile_no = request.GET['mobile_no']
        userentry.password = request.GET['password']
        userentry.creation_date = timezone.now()
        userentry.save()
        return home(request)
    else:
        return home(request)


def Login(request):
    userdata = user.objects.get(mobile_no=request.POST['mobile_no'])
    if userdata.password == request.POST['password']:
        request.session['name'] = userdata.name
        request.session['userid'] = userdata.id
        data = blog_data.objects.filter(
            userid=userdata.id).order_by('-creation_date')
        # if data.count() > 0:
        return render(request, 'blog/share.html', {'data': data, 'username': userdata.name})
        # else:
        # return render(request, 'blog/share.html', {'data:not found'})
        # return render(request, 'blog/share.html')
    else:
        return render(request, 'blog1/home.html', {'data': "incorrect mobile number or password"})


def Logout(request):
    try:
        del request.session['name']
        del request.session['userid']
        return render(request, 'blog1/home.html')
    except KeyError:
        pass
    return render(request, 'blog1/home.html')


def Share(request):
    id = request.session['userid']
    if id:
        data = blog_data.objects.filter(
            userid=id).order_by('-creation_date')
        if data.count() > 0:
            return render(request, 'blog/share.html', {'data': data, 'hide': "hide"})
        else:
            return HttpResponse("no notes found.")
    else:
        return render(request, 'blog/home.html')


def Save_notes(request):
    postdata = blog_data()
    id = request.session['userid']
    postdata.userid = request.session['userid']
    postdata.username = request.session['name']
    # postdata.blog_title = request.GET['title']
    postdata.blog_notes = request.GET['notes']
    postdata.creation_date = timezone.now()
    postdata.updation_date = timezone.now()
    postdata.deletedstatuse = 0
    postdata.save()
    return Share(request)

    # return render(request, 'blog/home.html')


def Update_notes(request):
    postdata = blog_data.objects.get(id=request.GET['id'])
    postdata.blog_notes = request.GET['notes']
    postdata.updation_date = timezone.now()
    postdata.save()
    return Share(request)


def Delete_notes(request):
    postdata = blog_data.objects.get(id=request.GET['id'])
    postdata.delete()
    return Share(request)


def Share_option(request):
    userdata = user.objects.all().order_by('id')
    userid =request.session['userid']
    notes_id = request.GET['notes_id']
    return render(request, 'blog/share_option.html', {'userdata': userdata, 'notes_id': notes_id,'userid':userid })


def Share_option_save(request):
    notes_id = float(request.GET['notes_id'])
    postdata = blog_data.objects.get(id=notes_id)
    if request.GET['check'] == "0":
        postdata.sharetoReadOnly = postdata.sharetoReadOnly + \
            "|" + request.GET['strp']+"|"
        postdata.save()
        return Share(request)
    else:
        postdata.sharetoRW = postdata.sharetoRW+"|" + request.GET['strp']+"|"
        postdata.save()
        return HttpResponse("data")


def SharedToMe(request):
    userid = request.session['userid']
    id = "|"+str(userid)+"|"
    notesdata = blog_data.objects.all()
    # notesdata = blog_data.objects.get(sharetoReadOnly__contains=id)
    # return render(request, 'blog/sharedToMe.html', {'notesdata': notesdata,'userid':userid})
    return render(request, 'blog/sharedToMe.html', {'notesdata': notesdata, 'userid': id})
