from rest_framework import generics
from adoptions.models import AdoptionRequest
from adoptions.serializers import AdoptionRequestSerializer
from users.permissions import IsAdminOrEmpleado, IsAdminOnly
from rest_framework.permissions import IsAuthenticated

# Ver solicitudes (solo autenticados)
class AdoptionRequestListView(generics.ListAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]

# Crear solicitud (cualquier usuario autenticado)
class AdoptionRequestCreateView(generics.CreateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]

# Actualizar estado (solo admin y empleados)
class AdoptionRequestUpdateView(generics.RetrieveUpdateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAdminOrEmpleado]

# Eliminar solicitud (solo admin)
class AdoptionRequestDeleteView(generics.DestroyAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAdminOnly]
