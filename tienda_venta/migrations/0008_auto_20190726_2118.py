# Generated by Django 2.2.3 on 2019-07-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0007_auto_20190726_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente2',
            name='cedula',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
