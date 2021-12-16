# Generated by Django 3.2.9 on 2021-12-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrada', '0002_auto_20211128_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('barrio', models.CharField(max_length=20)),
                ('destino', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=20)),
                ('puntuacion', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=20)),
                ('email_empresa', models.EmailField(max_length=254)),
                ('tamano_camion', models.CharField(max_length=20)),
            ],
        ),
    ]
