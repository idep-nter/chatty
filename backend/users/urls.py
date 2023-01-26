from django.urls import include, path
from rest_framework import routers

from .views import UserIdView, CustomUserViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='Users')

urlpatterns = [
    path('userId/', UserIdView.as_view(), name='UserIdView'),
    path('', include(router.urls))
]