# Generated by Django 4.2 on 2024-11-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0014_alter_fooditem_price_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
