from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Post(models.Model):
    name = models.CharField(max_length=200)
    desc=models.TextField()