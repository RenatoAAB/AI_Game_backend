# serializers.py
from rest_framework import serializers
from .models import Carta, Comportamento, Tipo, Ataque

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

    def create(self, validated_data):
        tipo_data = validated_data.pop('tipo')
        tipo_instance = self.get_or_create_tipo(**tipo_data)
        ataque_instance = Ataque.objects.create(tipo=tipo_instance, **validated_data)
        return ataque_instance

    #A criação de um validador próprio se mostra necessária pois a unicidade determinada no modelo exige o get or create mais especifico
    def get_or_create_tipo(self, **tipo_data): 
        tipo_name = tipo_data.get('nome')
        tipo_instance, _ = Tipo.objects.get_or_create(nome=tipo_name)
        return tipo_instance


class CartaSerializer(serializers.ModelSerializer):
    comportamento = ComportamentoSerializer()
    tipo = TipoSerializer()
    ataque = AtaqueSerializer()

    class Meta:
        model = Carta
        fields = '__all__'

    def create(self, validated_data):
        comportamento_data = validated_data.pop('comportamento')
        tipo_data = validated_data.pop('tipo')
        ataque_data = validated_data.pop('ataque')

        comportamento_instance, _ = Comportamento.objects.get_or_create(**comportamento_data)
        tipo_instance, _ = Tipo.objects.get_or_create(**tipo_data)

        ataque_serializer = AtaqueSerializer(data={**ataque_data})
        ataque_serializer.is_valid(raise_exception=True)
        ataque_instance = ataque_serializer.save()

        carta_instance = Carta.objects.create(
            comportamento=comportamento_instance,
            tipo=tipo_instance,
            ataque=ataque_instance,
            **validated_data
        )
        return carta_instance