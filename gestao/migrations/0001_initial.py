# Generated by Django 5.1.5 on 2025-01-21 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
                ('cnh_numero', models.CharField(max_length=20, unique=True)),
                ('cnh_categoria', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('D', 'D'), ('E', 'E')], max_length=2)),
                ('cnh_validade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('origem', models.CharField(max_length=255)),
                ('destino', models.CharField(max_length=255)),
                ('horario_saida', models.TimeField()),
                ('horario_chegada', models.TimeField()),
                ('motorista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestao.motorista')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('escola', models.CharField(max_length=255)),
                ('endereco', models.TextField()),
                ('responsavel', models.CharField(max_length=255)),
                ('contato_responsavel', models.CharField(max_length=15)),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao.rota')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
                ('capacidade', models.IntegerField()),
                ('motorista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestao.motorista')),
            ],
        ),
        migrations.AddField(
            model_name='rota',
            name='veiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestao.veiculo'),
        ),
    ]
