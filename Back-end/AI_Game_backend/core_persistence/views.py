from django.shortcuts import render, HttpResponse
from .models import Carta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartaSerializer

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