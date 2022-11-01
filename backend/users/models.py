from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  image = models.URLField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  about_me = models.TextField(max_length=999)
  post_number = models.IntegerField(null=True)
  registration_date = models.DateField(null=True)


  def __str__(self):
        return self.username