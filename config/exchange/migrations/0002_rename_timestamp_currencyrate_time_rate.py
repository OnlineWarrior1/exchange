# Generated by Django 5.0.1 on 2024-01-23 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currencyrate',
            old_name='timestamp',
            new_name='time_rate',
        ),
    ]
