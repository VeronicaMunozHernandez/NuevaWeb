# Generated by Django 2.2.3 on 2019-07-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0006_auto_20190726_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente2',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
