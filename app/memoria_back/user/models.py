from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=40, blank=True)
    apellido = models.CharField(max_length=40, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    rol = models.CharField(max_length=20, blank=True)
    refTienda = models.IntegerField(default=-1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
