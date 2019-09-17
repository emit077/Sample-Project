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
        return render(request, 'blog/home.html')
    else:
        return render(request, 'blog/contact.html')


def Login(request):
    userdata = user.objects.get(mobile_no=request.POST['mobile_no'])
    if userdata.password == request.POST['password']:
        request.session['name'] = userdata.name
        request.session['userid'] = userdata.id
        # data = blog_data.objects.all().order_by('-creation_date')[:5]
        # filter(client=client_id)
        data = blog_data.objects.filter(
            userid=userdata.id).order_by('-creation_date')[:5]
        return render(request, 'blog/share.html', {'data': data, 'username': userdata.name})
        # return render(request, 'blog/share.html')
    else:
        return HttpResponse("Your username and password didn't match.")


def Share(request):
    id = request.session['userid']
    if id:
        data = blog_data.objects.filter(
            userid=id).order_by('-creation_date')[:5]
        return render(request, 'blog/share.html', {'data': data})
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
    data = blog_data.objects.filter(userid=id).order_by('-creation_date')[:5]
    return render(request, 'blog/share.html', {'data': data})

    # return render(request, 'blog/home.html')


def Update_notes(request):
    id = request.session['userid']
    postdata = blog_data.objects.get(id=request.GET['id'])
    postdata.blog_notes = request.GET['notes']
    postdata.updation_date = timezone.now()
    postdata.save()
    co = blog_data.objects.filter(userid=id).count()
    if co > 0:
        data = blog_data.objects.filter(
            userid=id).order_by('-creation_date')[:5]
        return render(request, 'blog/share.html', {'data': data, 'hide': "hide"})
    else:
        return HttpResponse("no data" + id)


def Delete_notes(request):
    id = request.session['userid']
    postdata = blog_data.objects.get(id=request.GET['id'])
    postdata.delete()
    data = blog_data.objects.filter(userid=id).order_by('-creation_date')[:5]
    return render(request, 'blog/share.html', {'data': data})
    # postdata.deletedstatuse=1
    # postdata.history="deleted by"+request.session['userid']+","+request.session['name']+", @"+timezone.now()
    # postdata.save

def Share_option(request):
    userdata=user.objects.all().order_by('id')
    notes_id=request.GET['notes_id']
    return render(request, 'blog/share_option.html', {'userdata': userdata,'notes_id':notes_id})


def Share_option_save(request):
    id = request.session['userid']
    notes_id = float(request.GET['notes_id'])
    postdata = blog_data.objects.get(id=notes_id)
    if request.GET['cheak']:
        postdata.sharetoRW = request.GET['str']
        postdata.save()
        return HttpResponse("go data")
    else:
        postdata.sharetoReadOnly = request.GET['str']
        return HttpResponse("no data")
        postdata.save()
    
    # data = blog_data.objects.filter(userid=id).order_by('-creation_date')[:5]
    # return render(request, 'blog/share.html', {'data': data})
