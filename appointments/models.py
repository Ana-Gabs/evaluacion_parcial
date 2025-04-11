from django.db import models
from users.models import CustomUser
from pets.models import Mascota


class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Programada'),
            ('completed', 'Completada'),
            ('cancelled', 'Cancelada')
        ],
        default='scheduled'
    )

    def __str__(self):
        return f"{self.user.username} con {self.pet.name} el {self.date.strftime('%Y-%m-%d %H:%M')}"
