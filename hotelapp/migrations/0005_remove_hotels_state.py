# Generated by Django 4.1.3 on 2024-01-31 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_alter_hotels_country_alter_hotels_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='state',
        ),
    ]
