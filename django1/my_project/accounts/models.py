from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileUser(models.Model):
    # user=models.OneToOneField(User, on_delete=models.CASCADE)
    # image=models.ImageField(upload_to='user/',default='user_default.jpg')
    pass
