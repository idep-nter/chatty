from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import CustomUserSerializer
from .models import CustomUser


class UserIdView(APIView):
    def get(self, request, format=None):
        id = request.user.id
        return Response(id)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer