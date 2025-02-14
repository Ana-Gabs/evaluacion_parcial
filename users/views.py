from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer
# ./user/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .permissions import IsAdminOrEmpleado  # Importamos el nuevo permiso personalizado

# Definir el permiso personalizado
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que permite solo a los administradores modificar
    los recursos de usuario, pero todos los usuarios autenticados pueden verlos.
    """

class UserViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar usuarios:
    - "Viewer" puede solo ver usuarios.
    - "Administrador" y "Empleado" pueden crear, actualizar y eliminar usuarios.
    """
    queryset = CustomUser.objects.all()  # Obtiene todos los usuarios
    serializer_class = UserSerializer  # Usa el serializador de usuarios
    permission_classes = [IsAdminOrEmpleado]  # Aplicamos el permiso personalizado

    def get_permissions(self):
        """
        Ajusta los permisos según el método HTTP.
        """
        if self.action == 'list':  # Acción GET -> Sin autenticación
            return [AllowAny()]  # Permitir acceso sin autenticación
        elif self.action == 'create':  # Acción POST -> Con autenticación
            return [IsAuthenticated()]  # Solo usuarios autenticados pueden crear usuarios
        else:
            return super().get_permissions()  # Usar permisos por defecto para otras acciones
        

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer  # Usa el serializador de registro
    permission_classes = [IsAdminOrEmpleado]  # Permitir el registro sin autenticación

    def post(self, request, *args, **kwargs):
        print(request.data)  # Imprimir los datos del registro para depuración
        return super().post(request, *args, **kwargs)