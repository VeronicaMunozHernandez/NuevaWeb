# Generated by Django 2.2.3 on 2019-07-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0005_auto_20190725_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
