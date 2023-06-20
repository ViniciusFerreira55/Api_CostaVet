from django.contrib import admin
from django.urls import path, include
from core.views import UsuarioViewSet, AnimalViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Animal', AnimalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
