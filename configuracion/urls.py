from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import logout_usuario

# Importaciones explícitas para evitar errores
from eventos.views import (
    pagina_principal, 
    lista_eventos, 
    inscribir_evento, 
    mis_inscripciones, 
    cancelar_inscripcion
)
from usuarios.views import registro_usuario

urlpatterns = [
    # Panel administrativo
    path('admin/', admin.site.urls),
    
    # Páginas principales
    path('', pagina_principal, name='inicio'),
    path('eventos/', lista_eventos, name='lista_eventos'),
    
    # Autenticación y usuarios
    path('registro/', registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', logout_usuario, name='logout'),
    
    # Gestión de eventos
    path('inscribir/<int:evento_id>/', inscribir_evento, name='inscribir_evento'),
    path('mis-inscripciones/', mis_inscripciones, name='mis_inscripciones'),
    path('cancelar/<int:inscripcion_id>/', cancelar_inscripcion, name='cancelar_inscripcion'),
]