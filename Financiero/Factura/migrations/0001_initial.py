# Generated by Django 2.2.22 on 2021-05-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('info', models.CharField(max_length=255)),
                ('pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Pago.Pago')),
            ],
        ),
    ]
