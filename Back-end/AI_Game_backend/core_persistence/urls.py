from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('cartas', views.all_cards, name='cartas'),
    path('howmanycards', views.how_many_cards, name='how_many'),
    path('carta', views.CartaViews.as_view(), name = 'carta')
]

#importante configurar corretamente
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)