# ./user/views.py

from rest_framework import status, views
from rest_framework.response import Response
from .serializers import CustomUserSerializer

class RegisterUserView(views.APIView):
    """
    Vista para registrar un nuevo usuario.
    """

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Usuario creado exitosamente",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
