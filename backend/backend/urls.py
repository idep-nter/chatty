from django.contrib import admin
from django.urls import path, include
from chatty import urls as chatty_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(chatty_urls)),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
]
