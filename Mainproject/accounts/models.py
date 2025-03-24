from django.db import models
from django.conf import settings  # Correct way to reference the custom user model
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    """Artist model for hire"""
    name = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    image = models.ImageField(upload_to="artists/", blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Fix here

    def __str__(self):
        return self.name
    


class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser"""
    phone = models.CharField(max_length=15, blank=True, null=True)
