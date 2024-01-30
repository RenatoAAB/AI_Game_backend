from django.shortcuts import render, HttpResponse
from .models import Carta, Deck, CardInDeck, Ataque, Tipo, Comportamento
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartaSerializer, DeckSerializer, CardInDeckSerializer, ComportamentoSerializer, TipoSerializer, AtaqueSerializer
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView

# Create your views here.
# views é onde eu tenho requests pra pegar os dados e tals


def home(request):
    return render(request, 'home.html')


def all_cards(request):
    cartas = Carta.objects.all()
    return render(request, 'all_cards.html', {'cards' : cartas})

def how_many_cards(request):
    cartas = Carta.objects.all()
    return Response(len(cartas), status=status.HTTP_204_NO_CONTENT)


class CartaDetailView(RetrieveAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer

class CartaViews(APIView):
    def post(self, request, format=None):
        serializer = CartaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        try:
            nome = request.data.get('nome', None)
            carta = Carta.objects.get(nome=nome)
        except Carta.DoesNotExist:
            return Response({'error': 'Carta not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(carta, status=status.HTTP_204_NO_CONTENT)
    
    def delete(self, request, format=None):
        try:
            nome = request.data.get('nome', None)
            carta = Carta.objects.get(nome=nome)
        except Carta.DoesNotExist:
            return Response({'error': 'Carta not found'}, status=status.HTTP_404_NOT_FOUND)
        carta.delete()
        return Response({'success': 'Carta deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class DeckViews(APIView):
    def post(self, request, format=None):
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        nome = request.data.get('nome', None)
        if nome:
            try:
                deck = Deck.objects.get(nome=nome)
                deck.delete()
                return Response({'success': 'Deck deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Deck.DoesNotExist:
                return Response({'error': 'Deck not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
    
class CardInDeckViews(APIView):
    def post(self, request, format=None):
        serializer = CardInDeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        cards_in_deck = CardInDeck.objects.all()
        serializer = CardInDeckSerializer(cards_in_deck, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        deck_name = request.data.get('deck_name', None)
        position = request.data.get('position', None)

        if deck_name and position:
            try:
                deck = Deck.objects.get(nome=deck_name)
                card_in_deck = CardInDeck.objects.get(deck=deck, position=position)
                card_in_deck.delete()
                return Response({'success': 'Card removed from deck successfully'}, status=status.HTTP_204_NO_CONTENT)
            except (Deck.DoesNotExist, CardInDeck.DoesNotExist):
                return Response({'error': 'Deck or Card in Deck not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Deck name and position are required'}, status=status.HTTP_400_BAD_REQUEST)
    
class DeckDetailView(RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class CardInDeckDetailView(RetrieveAPIView):
    queryset = CardInDeck.objects.all()
    serializer_class = CardInDeckSerializer

class CardInDeckCreateView(CreateAPIView):
    queryset = CardInDeck.objects.all()
    serializer_class = CardInDeckSerializer

class DeckCreateView(CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckDeleteView(DestroyAPIView):
    queryset = Deck.objects.all()
    lookup_field = 'pk'


class ComportamentoViews(APIView):
    def post(self, request, format=None):
        serializer = ComportamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, nome):
        comportamento = Comportamento.objects.get(nome = nome)
        serializer = ComportamentoSerializer(comportamento)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TipoViews(APIView):
    def post(self, request, format=None):
        serializer = TipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        tipos = Tipo.objects.all()
        serializer = TipoSerializer(tipos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AtaqueViews(APIView):
    def post(self, request, format=None):
        serializer = AtaqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        ataques = Ataque.objects.all()
        serializer = AtaqueSerializer(ataques, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)