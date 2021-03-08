from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    Name = models.CharField(max_length=50)
    username =models.CharField(max_length=25)
    mail = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.Name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postName = models.CharField(max_length=100)
    postContent = models.TextField()
    postCreate = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.postName