# ./user/serializers.py
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hacemos role opcional y sin required
        self.fields['role'] = serializers.ChoiceField(
            choices=CustomUser.Roles.choices,
            required=False
        )

    def validate_role(self, value):
        request = self.context.get('request')

        # Si no se especifica un rol, se asume Viewer (por defecto)
        if not value:
            return CustomUser.Roles.VIEWER

        # Si se especifica Admin o Employee y el usuario no es admin autenticado
        if value in [CustomUser.Roles.ADMIN, CustomUser.Roles.EMPLOYEE]:
            if not request or not request.user.is_authenticated or not request.user.is_admin():
                raise serializers.ValidationError("Solo los administradores pueden asignar este rol.")

        return value

    def create(self, validated_data):
        # Si no vino rol, se pone Viewer por defecto
        role = validated_data.get('role', CustomUser.Roles.VIEWER)

        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            second_last_name=validated_data.get('second_last_name', ''),
            role=role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
