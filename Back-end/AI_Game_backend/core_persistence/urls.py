from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cartas', views.all_cards, name='cartas'),
    path('howmanycards', views.how_many_cards, name='how_many'),
    path('carta', views.CartaViews.as_view(), name = 'carta')
]