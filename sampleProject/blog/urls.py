from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('MyNotes/', views.login, name='blog-login'),
    path('login_form/', views.login_form, name='blog-login_form'),
    path('forgetpass/', views.forgetpass, name='blog-forgetpass'),
    path('resetpass/', views.resetpass, name='blog-resetpass'),
    path('register_form/', views.register_form, name='blog-register_form'),
    path('registration/', views.registration, name='blog-registration'),
    path('verifyuser/', views.verifyuser, name='blog-verifyuser'),
    path('user_post/', views.user_post, name='blog-user_post'),
    path('Share/', views.Share, name='blog-Share'),
    path('Save_notes/', views.Save_notes, name='blog-Save_notes'),
    path('Delete_notes/', views.Delete_notes, name='blog-Delete_notes'),
    path('Logout', views.Logout, name='blog-Logout'),
    path('SearchUser/', views.SearchUser, name='blog-SearchUser'),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('delete/', views.delete_session, name='blog-delete'),
    path('userprofile/', views.userprofile, name='blog-userprofile'),
    path('con_request/', views.con_request, name='blog-con_request'),
    path('conrequiestList/', views.conrequiestList, name='blog-conrequiestList'),
    path('comment_save/', views.comment_save, name='blog-comment_save'),
    path('like_post/', views.like_post, name='blog-like_post'),
    path('accept_reject_request/', views.accept_reject_request,
         name='blog-accept_reject_request'),
    path('likedby/', views.likedby, name='blog-likedby'),
    path('commentsby/', views.commentsby, name='blog-commentsby'),


]
