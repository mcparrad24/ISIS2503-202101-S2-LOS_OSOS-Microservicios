# Generated by Django 3.1.7 on 2021-05-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='info',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
