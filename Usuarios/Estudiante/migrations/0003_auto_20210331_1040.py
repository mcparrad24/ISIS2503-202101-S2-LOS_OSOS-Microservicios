# Generated by Django 2.2 on 2021-03-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0002_auto_20210331_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
