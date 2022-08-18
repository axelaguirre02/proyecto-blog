from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm


def inicio(request):

    return render(request, 'principal/inicio.html', {})


def registrar_pagina(request):

    if request.user.is_authenticated:

        return redirect('inicio')
    
    else:

        form_registro = RegistroForm()

        if request.method == 'POST':
            form_registro = RegistroForm(request.POST)

            if form_registro.is_valid():
                form_registro.save()

                messages.success(request, '¡Registro exitoso!')

                return redirect('inicio')


    return render(request, 'usuarios/registro.html', {'form_registro': form_registro})


def pagina_login(request):

    if request.user.is_authenticated:

        return redirect('inicio')
    
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)    

            if user is not None:
                login(request, user)
                return redirect('inicio')

            else:
                messages.warning(request, '¡Registro incorrecto!')


    return render(request, 'usuarios/pagina_login.html', {})


def logout_user(request):

    logout(request)

    return redirect('ingreso')

