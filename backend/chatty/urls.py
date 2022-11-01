from django.urls import include, path
from rest_framework import routers

from .views import ThreadViewSet, PostViewSet, TagViewSet


router = routers.DefaultRouter()
router.register(r'threads', ThreadViewSet, basename='Thread')
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'tags', TagViewSet, basename='Tags')

urlpatterns = [
    path('', include(router.urls)),
]
