from rest_framework import generics
from pets.models import Pet
from pets.serializers import PetSerializer
from users.permissions import IsAdminOrEmpleado, IsAdminOnly
from rest_framework.permissions import IsAuthenticated

# listar mascotas (todos los autenticados)
class PetListView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

# crear mascota (solo admin y empleado)
class PetCreateView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrEmpleado]

# editar mascota (solo admin y empleado)
class PetUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrEmpleado]

# eliminar mascota (solo admin)
class PetDeleteView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOnly]

