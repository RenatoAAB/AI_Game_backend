from django.contrib import admin
from .models import Carta, Tipo, Comportamento, Ataque

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Comportamento)
admin.site.register(Ataque)
admin.site.register(Carta)

