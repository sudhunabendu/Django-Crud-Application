from django.db import models

# Create your models here.
class Crud(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()
