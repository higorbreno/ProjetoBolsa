from rest_framework import serializers
from .models import Equipamento, Mes, EquipamentoEficiencia

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = (
            'id',
            'created',
            'latitude',
            'longitude'
        )

class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mes
        fields = (
            'id',
            'created',
            'title',
            'mes'
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