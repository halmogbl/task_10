# Generated by Django 2.1.5 on 2019-02-17 10:36

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20190217_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.Restaurant'),
        ),
    ]
