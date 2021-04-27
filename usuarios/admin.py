from django.contrib import admin
from usuarios.models import Usuario # dentro da pasta usuário, no arquivo models importar  classe Usuário


admin.site.register(Usuario) #registrar no painel admin as modificações de usuário do model
