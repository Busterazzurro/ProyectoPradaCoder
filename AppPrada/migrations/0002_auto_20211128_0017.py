# Generated by Django 3.2.9 on 2021-11-28 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrada', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viaje',
            old_name='ubicacion_retiro',
            new_name='destino',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='ubicacion_retorno',
            new_name='origen',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='pago_electronico',
            new_name='pago_online',
        ),
    ]