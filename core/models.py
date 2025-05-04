# core/models.py
from django.db import models

class CustomPokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name