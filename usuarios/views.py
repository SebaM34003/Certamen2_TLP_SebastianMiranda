from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente! 🎉')
            return redirect('lista_eventos')
    else:
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def logout_usuario(request):
    """Vista personalizada para logout con mensaje"""
    logout(request)
    messages.success(request, '¡Has cerrado sesión correctamente!')
    return redirect('inicio')  # o return redirect('/')