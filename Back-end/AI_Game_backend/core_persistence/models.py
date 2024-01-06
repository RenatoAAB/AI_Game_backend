from django.db import models

# Create your models here.

class Carta(models.Model):
    nome = models.CharField(max_length=200)
    custo = models.IntegerField()
    vida = models.IntegerField()
    ataque = models.IntegerField() #será trocado por uma reference no futuro
    agilidade = models.IntegerField()