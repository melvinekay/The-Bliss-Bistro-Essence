# Generated by Django 4.2 on 2024-11-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
