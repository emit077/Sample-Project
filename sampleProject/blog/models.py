from django.db import models

# Create your models here.


class user(models.Model):
    userid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)
    creation_date = models.DateTimeField()



class blog_data(models.Model):
    userid = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    # blog_title = models.CharField(max_length=100)
    blog_notes = models.TextField(max_length=None)
    sharedwith = models.TextField(max_length= None)
    notsharedwith = models.TextField(max_length=None)
    creation_date = models.DateTimeField()
    updation_date = models.DateTimeField()
    history = models.TextField(max_length=None)
    deletedstatuse=models.BooleanField()
