# Generated by Django 3.2 on 2021-04-14 23:21

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=194, unique=True, verbose_name='E-mail do usuário')),
                ('is_active', models.BooleanField(default=True, verbose_name='Usuário está ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuário é da equipe de desenvolvimento')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Usuário é um superusuário')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'usuario',
            },
            bases=(models.Model, django.contrib.auth.models.PermissionMixin),
        ),
    ]
