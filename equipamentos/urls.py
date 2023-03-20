from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from equipamentos import views

urlpatterns = [
    path('equipamentos/', views.EquipamentoList.as_view()),
    path('equipamentos/<int:pk>/', views.EquipamentoDetail.as_view()),
    path('equipamentos/eficiencia/', views.EquipamentoEficienciaList.as_view()),
    path('equipamentos/eficiencia/<int:pk>/', views.EquipamentoEficienciaDetail.as_view()),
    path('mes/', views.MesList.as_view()),
    path('mes/<int:pk>/', views.MesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)