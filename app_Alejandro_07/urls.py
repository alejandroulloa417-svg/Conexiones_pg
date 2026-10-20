from django.urls import path
from . import views

urlpatterns = [
    path('evaluaciones/', views.listar_evaluaciones, name='listar_evaluaciones'),
    path('evaluaciones/crear/', views.crear_evaluacion, name='crear_evaluacion'),
    path('ubicaciones/', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('ubicaciones/registrar/', views.registrar_ubicacion, name='registrar_ubicacion'),
]