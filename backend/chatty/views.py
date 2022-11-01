from django.shortcuts import render
from urllib import request
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializer import ThreadSerializer, TagSerializer, PostSerializer
from .models import Thread, Tag, Post


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ThreadPagination(PageNumberPagination):
    page_size = 10


class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(thread=self.thread) 


class ThreadPagination(PageNumberPagination):
    page_size = 10  

  
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer