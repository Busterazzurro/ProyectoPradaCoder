# Generated by Django 3.2.9 on 2021-12-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrada', '0004_auto_20211210_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='puntuacion',
            field=models.CharField(max_length=1),
        ),
    ]