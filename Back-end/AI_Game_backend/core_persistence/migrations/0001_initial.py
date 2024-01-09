# Generated by Django 5.0.1 on 2024-01-09 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ataque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('valor', models.IntegerField()),
                ('isAOE', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comportamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='padrao', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='carne', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('custo', models.IntegerField()),
                ('vida', models.IntegerField()),
                ('agilidade', models.IntegerField()),
                ('attack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_persistence.ataque')),
                ('comportamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_persistence.comportamento')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_persistence.tipo')),
            ],
        ),
        migrations.AddField(
            model_name='ataque',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_persistence.tipo'),
        ),
    ]
