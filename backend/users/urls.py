from django.urls import include, path
from rest_framework import routers

from .views import UserIdView, CustomUserViewSet, psw_check


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='Users')


urlpatterns = [
    path('user-id/', UserIdView.as_view(), name='UserIdView'),
    path('check-password/', psw_check, name='CheckPassword'),
    path('', include(router.urls))
]
