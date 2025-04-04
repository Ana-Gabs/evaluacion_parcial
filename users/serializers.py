# ./user/serializers.py
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)  # Añadimos el campo role como solo lectura

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'second_last_name', 'role']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=['Empleado', 'Viewer'], default='Viewer')  # Valor por defecto


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'second_last_name', 'role']

    def validate(self, data):
        """
        Validación personalizada para asegurarse de que los campos obligatorios estén presentes.
        """
        if not data.get('first_name'):
            raise serializers.ValidationError("El campo 'first_name' es obligatorio.")
        if not data.get('last_name'):
            raise serializers.ValidationError("El campo 'last_name' es obligatorio.")
        return data

    def create(self, validated_data):
        print("Datos validados:", validated_data)  # Verifica los datos recibidos
        role = validated_data.get('role', 'Viewer')  # Usar el valor por defecto solo si no está presente
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            second_last_name=validated_data.get('second_last_name', '')
        )

        # Asignar el grupo basado en el rol proporcionado
        group = Group.objects.get(name=role)
        user.groups.add(group)

        return user
