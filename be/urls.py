from django.contrib import admin
from django.urls import path, include
from core.views import UsuarioAPIView, AnimalAPIView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('usuario/', UsuarioAPIView.as_view()),
    path('animal/', AnimalAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('authentication/create/', include('djoser.urls')),
    path('authentication/created/', include('djoser.urls.authtoken')),
]


