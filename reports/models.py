from django.db import models
from users.models import CustomUser
from pets.models import Pet

class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte: {self.title} ({self.pet.name})"
