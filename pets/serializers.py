# pets/serializers.py
from rest_framework import serializers
from .models import Mascota
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'  # Serializamos todos los campos de la mascota

# Clase Factory, si la necesitas
class MascotaFactory:
    @staticmethod
    def crear_mascota(data):
        especie = data.get('especie')

        if especie not in dict(Mascota.ESPECIES):
            raise ValueError("Especie no soportada.")

        mascota = Mascota.objects.create(**data)
        return mascota
