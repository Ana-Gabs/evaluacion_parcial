# ./user/urls.py
from django.urls import path, include
from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet) # Endpoint para usuarios

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Ruta de registro
    path('', include(router.urls)),  # Incluye las rutas de ViewSets
]
