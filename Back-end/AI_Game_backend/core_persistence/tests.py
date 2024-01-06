from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Carta

class CartaCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_carta(self):
        # Define the data you want to send in the POST request
        carta_data = {
            'nome': 'Guerreiro fedido',
            'agilidade': 5,
            'ataque': 3,
            'vida' : 6,
            'custo' : 4
            # Add other fields as needed
        }

        # Send a POST request to the create_carta endpoint
        response = self.client.post(reverse('create_carta'), carta_data, format='json') #reverse é pra sair do nome e pegar a url

        # Check that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that a Carta object was created in the database
        self.assertEqual(Carta.objects.count(), 1)

        # Optionally, you can check other details in the response or database if needed
        # Example: self.assertEqual(response.data['field1'], 'value1')

        # Clean up: Delete the created Carta object to keep the database clean
        #carta = Carta.objects.first()
        #carta.delete()