from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = models.CharField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255, null=True)
  last_name = models.CharField(max_length=255, null=True)
  image = models.URLField(max_length=255, null=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  about_me = models.TextField(max_length=999, null=True)
  number_of_posts = models.IntegerField(null=True)
  # registration_date = models.DateField(null=True)

  def __str__(self):
        return self.username