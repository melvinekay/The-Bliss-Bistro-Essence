# Generated by Django 4.2 on 2024-11-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0005_alter_booking_people_alter_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=16),
        ),
    ]