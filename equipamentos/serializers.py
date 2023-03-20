from rest_framework import serializers
from .models import Equipamento, EquipamentoEficiencia

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = (
            'id',
            'latitude',
            'longitude'
        )

class EquipamentoEficienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipamentoEficiencia
        fields = (
            'id',
            'equipamento',
            'mes',
            'eficiencia'
        )