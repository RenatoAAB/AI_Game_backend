from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cartas', views.all_cards, name='cartas'),
    path('create_carta', views.CartaCreateView.as_view(), name = 'create_carta')
]