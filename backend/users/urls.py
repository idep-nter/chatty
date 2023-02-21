from django.urls import include, path
from rest_framework import routers

from .views import UserIdView, CustomUserViewSet, psw_check, get_online_users


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='Users')


urlpatterns = [
    path('user-id/', UserIdView.as_view(), name='UserIdView'),
    path('check-password/', psw_check, name='CheckPassword'),
    path('online-users/', get_online_users, name='OnlineUsers'),
    path('', include(router.urls))
]
