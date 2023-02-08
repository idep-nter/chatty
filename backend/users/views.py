from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .serializer import CustomUserSerializer
from .models import CustomUser


@csrf_exempt
@api_view(['GET', 'POST'])
def psw_check(request):
    if request.method == 'POST':
        psw = request.user.password
        psw2 = request.data['psw']
        check = check_password(psw2, psw)
        return HttpResponse(check)


class UserIdView(APIView):
    def get(self, request, format=None):
        id = request.user.id
        return Response(id)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
