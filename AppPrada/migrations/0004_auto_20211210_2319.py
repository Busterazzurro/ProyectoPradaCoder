# Generated by Django 3.2.9 on 2021-12-10 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrada', '0003_clientes_comentarios_empresas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Viaje',
        ),
    ]
