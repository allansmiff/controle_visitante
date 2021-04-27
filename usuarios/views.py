from django.shortcuts import render
from visitantes.models import Visitante

def index (request):

    todos_visitantes = Visitante.objects.all()

    #context serve para mudar algo na página html
    context = {
        "nome_pagina": "Allan Smiff",
        "todos_visitantes": todos_visitantes,
    }
    return render(request, "index.html", context)