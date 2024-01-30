from django.db import models

# Create your models here.
local_teste = 'ImagensTeste'

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
    imagem = models.ImageField(upload_to=local_teste, null=True, blank=True)
    nome = models.CharField(max_length=200)
    custo = models.IntegerField()
    vida = models.IntegerField()
    comportamento = models.ForeignKey(Comportamento, on_delete=models.CASCADE, null=True) 
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)#null=True é importante para migrações...
    ataque = models.ForeignKey(Ataque, on_delete=models.CASCADE, null=True) #dar o mesmo nome é ruim !!!
    agilidade = models.IntegerField()


# model that represents a deck of cards(Carta). It saves the card position - 1 to 5
class Deck(models.Model):
    nome = models.CharField(max_length=200)

class CardInDeck(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    carta = models.ForeignKey(Carta, on_delete=models.CASCADE)
    position = models.IntegerField()

    class Meta:
        unique_together = ('deck', 'position')
