# ./user/views.py

from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request}
