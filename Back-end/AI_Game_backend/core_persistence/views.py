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


class CartaCreateView(APIView):
    def post(self, request, format=None):
        serializer = CartaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)