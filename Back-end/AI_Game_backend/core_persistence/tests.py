from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Carta, Comportamento, Tipo, Ataque, Deck, CardInDeck
import json

class CartaCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        # Clean up entries from other models
        Comportamento.objects.all().delete()
        Tipo.objects.all().delete()
        Ataque.objects.all().delete()
        Carta.objects.all().delete()

class CartaCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def setUp(self):
        self.carta_data = {
            'comportamento': 
                {'nome':'agressivo'},
            'tipo': 
                {'nome':'carne'},
            'ataque': 
                {'nome':'Fireball', 
                 'tipo': 
                    {'nome': 'fogo'}, 
                'valor': 3, 
                'isAOE': False},
            'nome': 'Mago de fogo aprendiz',
            'custo': 2,
            'agilidade':7,
            'vida':3
            # Add other fields as needed
        }

    def test_create_carta(self):
        #Precisei disso para fazer o django usar um parser adequado e não perder informações do json
        response = self.client.post(reverse('carta-create'), json.dumps(self.carta_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Carta.objects.count(), 1)
        self.assertEqual(Tipo.objects.count(), 2) 
        self.assertEqual(Comportamento.objects.count(), 1)
        self.assertEqual(Ataque.objects.count(), 1)

    def tearDown(self):
        Carta.objects.all().delete()
        Comportamento.objects.all().delete()
        Tipo.objects.all().delete()
        Ataque.objects.all().delete()

    def test_get_carta(self):
        # Create a Carta instance
        response = self.client.post(reverse('carta-create'), json.dumps(self.carta_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get the id of the created Carta instance
        carta_id = response.data['id']
        response = self.client.get(reverse('carta-detail', kwargs={'pk': carta_id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.carta_data['nome'])



class DeckCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        Deck.objects.all().delete()

    def test_create_deck(self):
        # Define the data for creating a Deck instance
        deck_data = {
            'nome': 'My Deck',
            # Add other fields as needed
        }
        response = self.client.post(reverse('deck-create'), deck_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Deck.objects.count(), 1)

    def test_create_deck_without_name(self):
        # Define the data for creating a Deck instance without a name
        deck_data = {
            # No name field
        }
        response = self.client.post(reverse('deck-create'), deck_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Deck.objects.count(), 0)

    def test_delete_deck(self):
        # Create a Deck instance
        deck = Deck.objects.create(nome='My Deck')

        response = self.client.delete(reverse('deck-delete', kwargs={'pk': deck.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Deck.objects.count(), 0)

class CardInDeckCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.deck = Deck.objects.create(nome='My Deck')
        self.carta = {
            'comportamento': 
                {'nome':'agressivo'},
            'tipo': 
                {'nome':'carne'},
            'ataque': 
                {'nome':'Fireball', 
                 'tipo': 
                    {'nome': 'fogo'}, 
                'valor': 3, 
                'isAOE': False},
            'nome': 'Mago de fogo aprendiz',
            'custo': 2,
            'agilidade':7,
            'vida':3
            # Add other fields as needed
        }

    def tearDown(self):
        CardInDeck.objects.all().delete()
        Deck.objects.all().delete()
        Carta.objects.all().delete()

    def test_create_card_in_deck(self):
        card_in_deck_data = {
            'deck': {'nome': self.deck.nome},
            'carta': self.carta,
            'position': '1'
        }

        response = self.client.post(reverse('card_in_deck-create'), card_in_deck_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CardInDeck.objects.count(), 1)

    def test_create_card_in_deck_without_deck(self):
        card_in_deck_data = {
            'carta': self.carta
        }
        response = self.client.post(reverse('card_in_deck-create'), json.dumps(card_in_deck_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CardInDeck.objects.count(), 0)

    def test_create_card_in_deck_without_card(self):
        card_in_deck_data = {
            'deck': {'nome': self.deck.nome},
        }
        response = self.client.post(reverse('card_in_deck-create'), json.dumps(card_in_deck_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CardInDeck.objects.count(), 0)