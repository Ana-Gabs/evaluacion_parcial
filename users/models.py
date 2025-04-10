# ./user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        VIEWER = 'Viewer', 'Viewer'
        EMPLOYEE = 'Employee', 'Employee'
        ADMIN = 'Admin', 'Admin'

    email = models.EmailField(unique=True)
    second_last_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.VIEWER,
    )

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'second_last_name']

    def __str__(self):
        return self.username

    # Métodos de utilidad para permisos
    def is_admin(self):
        return self.role == self.Roles.ADMIN

    def is_employee(self):
        return self.role == self.Roles.EMPLOYEE

    def is_viewer(self):
        return self.role == self.Roles.VIEWER
