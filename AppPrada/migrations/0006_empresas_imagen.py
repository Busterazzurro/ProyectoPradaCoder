# Generated by Django 3.2.9 on 2021-12-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrada', '0005_alter_comentarios_puntuacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empresas'),
        ),
    ]