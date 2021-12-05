from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crud(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()

# class User(models.Model):
#     user_name = models.CharField(max_length=70)
#     password = models.CharField(max_length=70)

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    Page_name = models.CharField(max_length=70)
    Page_cat = models.CharField(max_length=70)
    Page_publish_date = models.DateField()