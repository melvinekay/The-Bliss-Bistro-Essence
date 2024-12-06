# Generated by Django 4.2 on 2024-12-02 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlissBistroApp', '0017_order_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='session_key',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BlissBistroApp.user'),
        ),
    ]
