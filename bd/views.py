from django.shortcuts import render

# Create your views here.

def inicio(peticion):
    return render (peticion, 'bd/inicio.html'   )