from django.db import models
# from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# from django_currentuser.db.models import CurrentUserField

from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=255)   

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(max_length=999)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # author = CurrentUserField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField(max_length=999)
    
    def __str__(self):
        return self.content[:20]