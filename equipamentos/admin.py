from django.contrib import admin
from .models import Equipamento, Mes, EquipamentoEficiencia

# Register your models here.
admin.site.register(Equipamento)
admin.site.register(Mes)
admin.site.register(EquipamentoEficiencia)