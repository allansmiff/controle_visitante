from django.db import models

class Porteiro(models.Model):

    usuario = models.OneToOneField( #relacionamento de 1 para 1 no BD

        "usuarios.Usuario",
        verbose_name= "Usuarios",

        #on_delete é o comportamento a ser adotado quando o objeto referenciado é excluído."""
        on_delete= models.PROTECT #proteje para não deletar os dados
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        #se eu colocar True em auto_now sempre que atualizar as informações
        #vai pedir pra atualizar a data de nascimento
        auto_now=False,
        auto_now_add=False,

    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return self.nome_completo
