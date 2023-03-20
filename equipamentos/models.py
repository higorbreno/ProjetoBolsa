from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Equipamento(models.Model):
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)

class EquipamentoEficiencia(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    mes = models.DateField()
    eficiencia = models.FloatField()