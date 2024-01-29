from django.urls import path
from . import views
from .views import CartaDetailView, DeckDetailView, CardInDeckDetailView, DeckCreateView, CardInDeckCreateView, DeckDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('cartas', views.all_cards, name='cartas'),
    path('howmanycards', views.how_many_cards, name='how_many'),
    path('carta/<int:pk>/', CartaDetailView.as_view(), name='carta-detail'),
    path('carta', views.CartaViews.as_view(), name = 'carta-create'),
    path('deck/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('card_in_deck/<int:pk>/', CardInDeckDetailView.as_view(), name='card_in_deck-detail'),
    path('deck/', DeckCreateView.as_view(), name='deck-create'),
    path('card_in_deck/', CardInDeckCreateView.as_view(), name='card_in_deck-create'),
    path('deck/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    path('comportamento/<str:nome>/', views.ComportamentoViews.as_view(), name='comportamento-detail'),
    path('comportamento/', views.ComportamentoViews.as_view(), name='comportamento-create')
]

#importante configurar corretamente
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)