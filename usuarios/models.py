from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
#as três classes a seguir vai ajudar a criar modelo de usuário com autenticação com e-mail e senh
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email) #vai evitar caracterespecial, maiscula
        )

        usuario.is_active =True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin): # A classe Usuário é uma subclasse de AbstractBaseUse e PermissionMixin
    email = models.EmailField(
        verbose_name="E-mail do usuário", #Nome do campo
        max_length=194, #Tamanho máximo do campo
        unique=True, # E-mail tem que ser único
    )

    is_active = models.BooleanField( #verifica se usuário esta ativo
        verbose_name="Usuário está ativo", #nome ao campo
        default=True, #verdadeiro
    )

    is_staff = models.BooleanField( #verifica se usuário é da equipe
        verbose_name="Usuário é da equipe de desenvolvimento", #label
        default=False, #falso
    )
    is_superuser = models.BooleanField( #verifica se é superusuario
        verbose_name="Usuário é um superusuário", #label
        default=False, #falso pq nem todos serao super
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager() #subscreveu o padrão do django informando que usuário manager é o padrão

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario" #organiza o nome da tabela, pra n criar padrão,tera o nome de usuário

    def __str__(self):
        return self.email