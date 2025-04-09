# ./user/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'second_last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """
        Validaciones adicionales para el registro de un nuevo usuario.
        """
        if not data.get('first_name'):
            raise serializers.ValidationError("El campo 'first_name' es obligatorio.")
        if not data.get('last_name'):
            raise serializers.ValidationError("El campo 'last_name' es obligatorio.")
        return data

    def create(self, validated_data):
        """
        Crea el usuario y asigna el rol basado en el campo 'role'.
        """
        role = validated_data.get('role')
        password = validated_data.pop('password')

        # Crear el usuario
        user = CustomUser.objects.create_user(**validated_data)
        
        # Asignar el grupo basado en el rol
        try:
            group = Group.objects.get(name=role)
        except Group.DoesNotExist:
            raise serializers.ValidationError(f"El rol '{role}' no existe.")
        
        user.groups.add(group)
        user.set_password(password)
        user.save()
        
        return user
