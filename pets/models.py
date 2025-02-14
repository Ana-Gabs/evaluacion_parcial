from django.db import models
from users.models import CustomUser  # Usuario que registra la mascota

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[('dog', 'Perro'), ('cat', 'Gato'), ('other', 'Otro')])
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)  # Si está disponible para adopción
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # Quién agregó la mascota
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
