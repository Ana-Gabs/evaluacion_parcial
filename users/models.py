# ./user/models.py
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    second_last_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
