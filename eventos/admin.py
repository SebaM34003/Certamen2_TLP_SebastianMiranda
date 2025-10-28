from django.contrib import admin
from .models import Evento, Inscripcion

class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 0
    readonly_fields = ['fecha_inscripcion']
    can_delete = False

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 
        'fecha_hora', 
        'lugar', 
        'precio', 
        'capacidad',
        'plazas_disponibles',
        'total_recaudado'
    ]
    list_filter = ['fecha_hora', 'lugar']
    search_fields = ['titulo', 'descripcion', 'lugar']
    readonly_fields = ['plazas_disponibles', 'total_recaudado']
    inlines = [InscripcionInline]
    
    def plazas_disponibles(self, obj):
        return obj.plazas_disponibles()
    plazas_disponibles.short_description = 'Plazas Disponibles'
    
    def total_recaudado(self, obj):
        return f"${obj.total_recaudado():.2f}"
    total_recaudado.short_description = 'Total Recaudado'

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'evento', 'fecha_inscripcion']
    list_filter = ['evento', 'fecha_inscripcion']
    search_fields = ['usuario__username', 'evento__titulo']
    readonly_fields = ['fecha_inscripcion']