# Generated by Django 2.2.22 on 2021-05-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grupo', '0001_initial'),
        ('Grado', '0001_initial'),
        ('Estudiante', '0002_auto_20210530_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='grado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Grado.Grado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Grupo.Grupo'),
            preserve_default=False,
        ),
    ]
