from django.db import models

# Create your models here.

class Comportamento(models.Model):
    nome = models.CharField(max_length=200, default='padrao')

# Tipo é o constituinte de um ataque ou o material do qual um monstro é feito, talvez seja bom mudar para enum
class Tipo(models.Model):
    nome = models.CharField(max_length=200, default='carne')


class Ataque(models.Model):
    nome = models.CharField(max_length=200) #talvez possa ser removido
    valor = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE) #se o tipo for deletado, o ataque será também - senao teremos erros
    isAOE = models.BooleanField()


class Carta(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    custo = models.IntegerField()
    vida = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    comportamento = models.ForeignKey(Comportamento, on_delete=models.CASCADE, null=True) #null=True é importante para migrações...
    ataque = models.ForeignKey(Ataque, on_delete=models.CASCADE, null=True) #dar o mesmo nome é ruim !!!
    agilidade = models.IntegerField()

