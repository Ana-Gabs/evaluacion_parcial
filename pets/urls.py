# pets/views.py# pets/urls.py
from django.urls import path
from .views import MascotaListCreateAPIView, MascotaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/', MascotaListCreateAPIView.as_view(), name='mascota_list_create'),
    path('api/<int:pk>/', MascotaRetrieveUpdateDestroyAPIView.as_view(), name='mascota_detail'),
]

