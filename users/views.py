# ./user/views.py
# ./user/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer
from django.core.exceptions import PermissionDenied

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Asegura que el usuario está autenticado

    def perform_create(self, serializer):
        user = self.request.user  # Usuario autenticado

        # Verifica si el usuario autenticado es un administrador
        if user.is_admin():  # Solo los administradores pueden crear usuarios Admin o Empleado
            # Si es un Admin, puedes crear usuarios con cualquier rol.
            role = serializer.validated_data.get('role')
            if role == CustomUser.Roles.ADMIN or role == CustomUser.Roles.EMPLOYEE:
                serializer.save()  # Si el rol es Admin o Empleado, se guarda el usuario
            else:
                serializer.save()  # Si no, se guarda normalmente
        else:
            # Los usuarios no administradores no pueden crear usuarios con rol de Admin o Empleado
            role = serializer.validated_data.get('role')
            if role == CustomUser.Roles.ADMIN or role == CustomUser.Roles.EMPLOYEE:
                raise PermissionDenied("No tienes permiso para asignar este rol.")
            else:
                serializer.save()  # Se guarda normalmente si el rol es Viewer o cualquier otro
