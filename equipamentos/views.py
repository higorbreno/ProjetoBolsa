from rest_framework import generics
from .models import Equipamento, Mes, EquipamentoEficiencia
from .serializers import EquipamentoSerializer, MesSerializer, EquipamentoEficienciaSerializer

# Create your views here.
class EquipamentoList(generics.ListCreateAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class EquipamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class MesList(generics.ListCreateAPIView):
    queryset = Mes.objects.all()
    serializer_class = MesSerializer

class MesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mes.objects.all()
    serializer_class = MesSerializer

class EquipamentoEficienciaList(generics.ListCreateAPIView):
    queryset = EquipamentoEficiencia.objects.all()
    serializer_class = EquipamentoEficienciaSerializer

class EquipamentoEficienciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipamentoEficiencia.objects.all()
    serializer_class = EquipamentoEficienciaSerializer