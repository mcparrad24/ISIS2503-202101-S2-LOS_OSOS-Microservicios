# Generated by Django 2.2.22 on 2021-05-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grado.Grado')),
            ],
        ),
    ]