# Generated by Django 5.0.1 on 2024-01-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_persistence', '0003_alter_ataque_nome_alter_comportamento_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carta',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='ImagensTeste'),
        ),
    ]
