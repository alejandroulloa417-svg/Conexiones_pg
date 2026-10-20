from django.db import models
from django.contrib.auth.models import User

class EvaluacionEmocional(models.Model):
    # Relación 1-N: Un usuario (o paciente) puede tener MUCHAS evaluaciones emocionales.
    # Usamos ForeignKey apuntando al modelo User de Django.
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='evaluaciones_emocionales'
    )
    
    # Si 'profesional' también es un usuario del sistema, puedes relacionarlo igual:
    profesional = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='evaluaciones_realizadas'
    )
    
    estado_afectivo = models.CharField(max_length=100)
    nivel_riesgo = models.CharField(max_length=50)
    necesidades_detectadas = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación - {self.usuario.username}"


class UbicacionPaciente(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ubicaciones")
    latitud = models.FloatField()
    longitud = models.FloatField()
    autorizacion = models.BooleanField(default=False)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    fecha_ubicacion = models.DateTimeField(auto_now_add=True)