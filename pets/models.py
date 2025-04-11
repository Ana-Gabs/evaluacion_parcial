# ./pets/models.py
from django.db import models

class Mascota(models.Model):
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    edad = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pets/images/', blank=True, null=True)
    adoptado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()})"
