from django.db import models
from users.models import CustomUser
from pets.models import Mascota


class AdoptionRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Persona que adopta
    pet = models.ForeignKey(Mascota, on_delete=models.CASCADE)  # Mascota solicitada
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pendiente'), ('approved', 'Aprobado'), ('rejected', 'Rechazado')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.pet.name} ({self.status})"
