#from .models import Mascota

class MascotaFactory:
    @staticmethod
    def crear_mascota(data):
        especie = data.get('especie')

        if especie not in dict(Mascota.ESPECIES):
            raise ValueError("Especie no soportada.")

        mascota = Mascota.objects.create(**data)
        return mascota

from .models import Mascota

class MascotaFactory:
    @staticmethod
    def crear_mascota(data):
        especie = data.get('especie')

        if especie not in dict(Mascota.ESPECIES):
            raise ValueError("Especie no soportada.")

        mascota = Mascota.objects.create(**data)
        return mascota
