from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import Evento, Inscripcion

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('fecha_hora')
    return render(request, 'eventos/lista_eventos.html', {
        'eventos': eventos,
        'es_publico': not request.user.is_authenticated
    })

@login_required
def inscribir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if evento.plazas_disponibles() <= 0:
        messages.error(request, 'No hay plazas disponibles para este evento.')
        return redirect('lista_eventos')
    
    try:
        Inscripcion.objects.create(usuario=request.user, evento=evento)
        messages.success(
            request, 
            f'✅ Te has registrado exitosamente en "{evento.titulo}". '
            f'Plazas restantes: {evento.plazas_disponibles()}'
        )
    except IntegrityError:
        messages.warning(request, 'Ya estás registrado en este evento.')
    
    return redirect('lista_eventos')

@login_required
def mis_inscripciones(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user).select_related('evento')
    return render(request, 'eventos/mis_inscripciones.html', {
        'inscripciones': inscripciones
    })

@login_required
def cancelar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id, usuario=request.user)
    evento_titulo = inscripcion.evento.titulo
    inscripcion.delete()
    messages.success(request, f'Inscripción cancelada para "{evento_titulo}".')
    return redirect('mis_inscripciones')