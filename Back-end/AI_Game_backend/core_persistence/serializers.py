# serializers.py
from rest_framework import serializers
from .models import Carta, Comportamento, Tipo, Ataque, Deck, CardInDeck

#parece que é aqui que a gente lida com essas dependencias dos modelos...

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class ComportamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comportamento
        fields = '__all__'

class AtaqueSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer()

    class Meta:
        model = Ataque
        fields = '__all__'
    
    # É para usar os outros serializers e validar os dados antes de criar o ataque
    def to_internal_value(self, data):
        tipo_data = data.get('tipo')
        tipo_serializer = TipoSerializer(data=tipo_data)

        if tipo_serializer.is_valid(raise_exception=True):
            data['tipo'] = tipo_serializer.validated_data

        return super().to_internal_value(data)

    def create(self, validated_data):
        tipo_data = validated_data.pop('tipo')
        tipo, _ = Tipo.objects.get_or_create(**tipo_data)
        ataque = Ataque.objects.create(tipo=tipo, **validated_data)
        return ataque


class CartaSerializer(serializers.ModelSerializer):
    comportamento = ComportamentoSerializer()
    tipo = TipoSerializer()
    ataque = AtaqueSerializer()

    class Meta:
        model = Carta
        fields = '__all__'

    def to_internal_value(self, data):
        comportamento_data = data.get('comportamento')
        tipo_data = data.get('tipo')
        ataque_data = data.get('ataque')

        comportamento_serializer = ComportamentoSerializer(data=comportamento_data)
        tipo_serializer = TipoSerializer(data=tipo_data)
        ataque_serializer = AtaqueSerializer(data=ataque_data)

        if comportamento_serializer.is_valid(raise_exception=True):
            data['comportamento'] = comportamento_serializer.validated_data

        if tipo_serializer.is_valid(raise_exception=True):
            data['tipo'] = tipo_serializer.validated_data

        if ataque_serializer.is_valid(raise_exception=True):
            data['ataque'] = ataque_serializer.validated_data
        return super().to_internal_value(data)

    def create(self, validated_data):
        comportamento_data = validated_data.pop('comportamento')
        tipo_data = validated_data.pop('tipo')
        ataque_data = validated_data.pop('ataque')

        comportamento, _ = Comportamento.objects.get_or_create(**comportamento_data)
        tipo, _ = Tipo.objects.get_or_create(**tipo_data)

        ataque_serializer = AtaqueSerializer(data=ataque_data)
        ataque_serializer.is_valid(raise_exception=True)
        ataque = ataque_serializer.save()

        carta = Carta.objects.create(
            comportamento=comportamento,
            tipo=tipo,
            ataque=ataque,
            **validated_data
        )
        return carta

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

class CardInDeckSerializer(serializers.ModelSerializer):
    deck = DeckSerializer()
    carta = CartaSerializer()

    class Meta:
        model = CardInDeck
        fields = '__all__'

    def to_internal_value(self, data):
        deck_data = data.get('deck')
        card_data = data.get('carta')

        deck_serializer = DeckSerializer(data=deck_data)
        card_serializer = CartaSerializer(data=card_data)

        if deck_serializer.is_valid(raise_exception=True):
            data['deck'] = deck_serializer.validated_data

        if card_serializer.is_valid(raise_exception=True):
            data['carta'] = card_serializer.validated_data

        return super().to_internal_value(data)

    def create(self, validated_data):
        deck_data = validated_data.pop('deck')
        card_data = validated_data.pop('carta')

        deck_instance, _ = Deck.objects.get_or_create(**deck_data)
        card_instance, _ = Carta.objects.get_or_create(**card_data)

        card_in_deck_instance = CardInDeck.objects.create(
            deck=deck_instance,
            carta=card_instance,
            **validated_data
        )
        return card_in_deck_instance