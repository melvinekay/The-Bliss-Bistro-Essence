# Generated by Django 4.2 on 2024-11-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
