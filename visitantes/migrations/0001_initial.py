# Generated by Django 3.2 on 2021-04-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=190, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero_casa', models.PositiveIntegerField(verbose_name='Número da Casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do Veiculo')),
                ('horario_chegada', models.DateTimeField(auto_now=True, verbose_name=' Hora da chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horario de saida do codomínio')),
                ('horario_permitido', models.DateTimeField(blank=True, null=True, verbose_name='Horario de autorização de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=190, null=True, verbose_name='Morador respponsável')),
                ('porteiro_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Porteiro responsável pelo registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]
