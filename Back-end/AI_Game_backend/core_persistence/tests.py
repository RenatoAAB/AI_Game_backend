from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Carta, Comportamento, Tipo, Ataque

class CartaCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        # Clean up entries from other models
        Comportamento.objects.all().delete()
        Tipo.objects.all().delete()
        Ataque.objects.all().delete()
        Carta.objects.all().delete()

    def test_create_carta(self):
        # Define the data for creating a Carta instance
        carta_data = {
            'comportamento': {'nome': 'agressivo'},
            'tipo': {'nome': 'carne'},
            'ataque': {'nome': 'Fireball', 'tipo': {'nome': 'fogo'}, 'valor':3, 'isAOE': False},
            'nome': 'Mago de fogo aprendiz',
            'custo': 2,
            'agilidade':7,
            'vida':3
            # Add other fields as needed
        }

        # Send a POST request to the create_carta endpoint
        response = self.client.post(reverse('carta'), carta_data, format='json')

        # Check that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that a Carta object was created in the database
        self.assertEqual(Carta.objects.count(), 1)
        self.assertEqual(Tipo.objects.count(), 2) #criou os 2 tipos
        self.assertEqual(Comportamento.objects.count(), 1)
        self.assertEqual(Ataque.objects.count(), 1)

        # Optionally, you can check other details in the response or database if needed
        # Example: self.assertEqual(response.data['comportamento']['name'], 'Aggressive')

        # No need to clean up Carta objects as they will be deleted in tearDown method

    def test_create_carta_tipo_repetido(self):
        
        carta_data = {
            'comportamento': {'nome': 'agressivo'},
            'tipo': {'nome': 'carne'},
            'ataque': {'nome': 'Voadora', 'tipo': {'nome': 'carne'}, 'valor':2, 'isAOE': False},
            'nome': 'Lutador maluco',
            'custo': 1,
            'agilidade':9,
            'vida':1}
        
        response = self.client.post(reverse('carta'), carta_data, format='json')
        print(str(response.data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Carta.objects.count(), 1)
        self.assertEqual(Tipo.objects.count(), 1) 
        self.assertEqual(Comportamento.objects.count(), 1)
        self.assertEqual(Ataque.objects.count(), 1)