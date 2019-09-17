from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('MyNotes/', views.Login, name='blog-Login'),
    path('Registration/', views.Registration, name='blog-Registration'),
    path('Share/', views.Share, name='blog-Share'),
    path('Save_notes/', views.Save_notes, name='blog-Save_notes'),
    path('Update_notes/', views.Update_notes, name='blog-Update_notes'),
    path('Delete_notes/', views.Delete_notes, name='blog-Delete_notes'),
    path('Share_option/', views.Share_option, name='blog-Share_option'),
    path('Share_option_save/', views.Share_option_save, name='blog-Share_option_save'),
]
