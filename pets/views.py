# pets/views.py
from rest_framework import viewsets
from .models import Mascota
from .serializers import MascotaSerializer
from rest_framework.permissions import AllowAny  # Importa AllowAny

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [AllowAny]  # Permite acceso a todos los usuarios, autenticados o no   