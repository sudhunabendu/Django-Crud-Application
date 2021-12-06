from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.deletion import CASCADE

# Create your models here.
class Crud(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()


class User(models.Model):
    username = models.CharField('username', max_length=100)
    email = models.CharField('email', max_length=100)
    password = models.CharField('password', max_length=100)   

class Blog(models.Model):
    # one to many relationship
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Post_title',max_length=100)
    description = models.TextField('post_description')
    post_date = models.DateField(default=date.today)
    name = models.CharField('name',max_length=100)


# class User(models.Model):
#     user_name = models.CharField(max_length=70)
#     password = models.CharField(max_length=70)

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    Page_name = models.CharField(max_length=70)
    Page_cat = models.CharField(max_length=70)
    Page_publish_date = models.DateField()


