#authentication/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from users.models import CustomUser

class EmailOrUsernameModelBackend(BaseBackend):
    """
    Permite la autenticación con email o username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Buscar usuario por email si parece ser una dirección de correo
            if "@" in username:
                user = CustomUser.objects.get(email=username)
            else:
                user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

        # Verifica la contraseña si el usuario existe
        if user and check_password(password, user.password):  
            return user

        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
