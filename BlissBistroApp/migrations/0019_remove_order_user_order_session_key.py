# Generated by Django 4.2 on 2024-12-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0018_remove_order_session_key_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
