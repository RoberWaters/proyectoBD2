from django.db import models

class Usuario(models.Model):
    ROLES = [
        ("Administrador", "Administrador"),
        ("Marketing", "Marketing"),
        ("Cliente", "Cliente"),
    ]

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  # Solo para simplificar; usar `hash` en producción
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username
