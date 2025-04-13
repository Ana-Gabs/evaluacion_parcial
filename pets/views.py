# pets/views.py
from rest_framework import generics
from .models import Mascota
from .serializers import MascotaSerializer

class MascotaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class MascotaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

