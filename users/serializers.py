from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    role = serializers.ChoiceField(choices=CustomUser.Roles.choices, required=False)  # Asegúrate de que sea opcional

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'second_last_name',
            'role'
        ]

    def create(self, validated_data):
        # Si no se ha proporcionado un 'role', se asigna por defecto el rol 'Viewer'
        role = validated_data.get('role', CustomUser.Roles.VIEWER)

        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            second_last_name=validated_data.get('second_last_name', ''),
            role=role,  # Asigna el rol aquí
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
