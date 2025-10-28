from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Evento")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    fecha_hora = models.DateTimeField(verbose_name="Fecha y Hora")
    lugar = models.CharField(max_length=200, verbose_name="Lugar")
    imagen = models.ImageField(upload_to='eventos/', verbose_name="Imagen", blank=True, null=True)
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Valor",
        validators=[MinValueValidator(0)]
    )
    capacidad = models.PositiveIntegerField(verbose_name="Cantidad de Plazas")
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha_hora']
    
    def plazas_disponibles(self):
        return self.capacidad - self.inscripciones.count()
    
    def total_recaudado(self):
        return self.inscripciones.count() * self.precio
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_hora.strftime('%d/%m/%Y')}"

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inscripciones")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    
    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ['usuario', 'evento']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.evento.titulo}"
        