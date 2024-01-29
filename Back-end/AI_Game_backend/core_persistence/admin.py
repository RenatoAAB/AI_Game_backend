from django.contrib import admin
from .models import Carta, Tipo, Comportamento, Ataque, Deck, CardInDeck

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Comportamento)
admin.site.register(Ataque)
admin.site.register(Carta)
admin.site.register(Deck)
admin.site.register(CardInDeck)


