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
    role = serializers.ChoiceField(
        choices=CustomUser.Roles.choices,
        required=False,
        default=CustomUser.Roles.VIEWER,
        allow_null=True
    )

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

    def validate(self, data):
        if 'role' not in data or not data['role']:
            data['role'] = CustomUser.Roles.VIEWER

        request = self.context.get('request')
        if data['role'] in [CustomUser.Roles.ADMIN, CustomUser.Roles.EMPLOYEE]:
            if not request or not request.user.is_authenticated or not request.user.is_admin():
                raise serializers.ValidationError({
                    'role': "Solo los administradores pueden asignar este rol."
                })

        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            second_last_name=validated_data.get('second_last_name', ''),
            role=validated_data.get('role', CustomUser.Roles.VIEWER)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
