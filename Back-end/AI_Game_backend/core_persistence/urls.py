from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cartas', views.all_cards, name='cartas'),
    path('howmanycards', views.how_many_cards, name='how_many'),
    path('create_carta', views.CartaCreateView.as_view(), name = 'create_carta'),
    path('remove_carta', views.CartaRemoveByName.as_view(), name = 'remove_carta')
]