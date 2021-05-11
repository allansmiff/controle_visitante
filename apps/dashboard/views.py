from django.shortcuts import render
from visitantes.models import Visitante

def index (request):

    todos_visitantes = Visitante.objects.all()

    visitante_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitante_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitante_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )

    #context serve para mudar algo na página html
    context = {
        "nome_pagina": "Allan Smiff",
        "todos_visitantes": todos_visitantes,
        "visitante_aguardando": visitante_aguardando.count(),
        "visitante_em_visita": visitante_em_visita.count(),
        "visitante_finalizado": visitante_finalizado.count(),

    }
    return render(request, "index.html", context)
