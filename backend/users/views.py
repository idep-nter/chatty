from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.contrib.auth.signals import user_logged_in, user_logged_out
# from django.dispatch import receiver
# from datetime import timedelta

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


@csrf_exempt
@api_view(['GET', 'POST'])
def get_online_users(request):
    if request.method == 'GET':
        online = request.online_now
        return Response(online)


class UserIdView(APIView):
    def get(self, request, format=None):
        id = request.user.id
        return Response(id)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# @receiver(user_logged_in)
# def got_online(sender, CustomUser, request, **kwargs):
#     CustomUser.is_online = True
#     CustomUser.save()

# @receiver(user_logged_out)
# def got_offline(sender, CustomUser, request, **kwargs):
#     CustomUser.is_online = False
#     CustomUser.save()
