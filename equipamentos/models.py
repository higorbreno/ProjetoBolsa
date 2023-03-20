from django.db import models

# Create your models here.
class Equipamento(models.Model):
    created = models.DateField(auto_now_add=True)
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.id

class Mes(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.TextField()
    mes = models.DateField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class EquipamentoEficiencia(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    eficiencia = models.FloatField()

    class Meta:
        ordering = ['equipamento']