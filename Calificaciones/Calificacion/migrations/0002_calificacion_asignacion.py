# Generated by Django 3.1.7 on 2021-05-08 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asignacion', '0001_initial'),
        ('Calificacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='asignacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Asignacion.asignacion'),
            preserve_default=False,
        ),
    ]
