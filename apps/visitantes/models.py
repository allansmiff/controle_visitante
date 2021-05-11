from django.db import models

class Visitante(models.Model):

    STATUS_VISITANTE =[
        ("AGUARDANDO", "Aguardando visitante"),
        ("EM_VISITA", "Em visita"),
        ("VISITA_FINALIZADA","Visita finalizada")
    ]
    status = models.CharField(
        verbose_name="Status",
        max_length=20,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO"
    )

    nome_completo =models.CharField(
        verbose_name="Nome Completo",
        max_length=190,
    )

    cpf = models.CharField(
        verbose_name= "CPF",
        max_length=11,
    )
    data_nascimento = models.DateField(
        verbose_name= "Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    numero_casa = models.PositiveIntegerField(
        verbose_name= "Número da Casa a ser visitada",
    )

    placa_veiculo = models.CharField(
        verbose_name= "Placa do Veiculo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name= " Hora da chegada na portaria",
        auto_now=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name= "Horario de saida do codomínio",
        auto_now=False,
        blank=True,
        null=True,
    )

    horario_permitido = models.DateTimeField(
        verbose_name= "Horario de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name= "Morador respponsável",
        max_length=190,
        blank=True,
        null=True,
    )

    porteiro_responsavel = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horario de saida não registrado"

    def get_horario_permitido(self):
        if self.horario_permitido:
            return self.horario_permitido

        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel

        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo

        return "Veiculo não registrado"

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]

            cpf_formatado = f"{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}"
            return cpf_formatado


    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo