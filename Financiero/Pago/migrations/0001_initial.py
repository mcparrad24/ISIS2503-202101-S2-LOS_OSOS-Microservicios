# Generated by Django 2.2.22 on 2021-05-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('acudienteEmail', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]