
from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import (
    registrar_visitante, informacoes_visitante
)


urlpatterns = [
    path(
        "admin/",
         admin.site.urls
         ),

    path(
        "",
         index,
         name="index",
         ),

    path(
        "registrar-visitante/",#aparece na url do navegador
        registrar_visitante, #rotorna a visão de view
        name="registrar_visitante",
        ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitante,
        name="informacoes_visitante",
        ),
]
