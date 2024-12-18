# Generated by Django 4.2.16 on 2024-10-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airlines", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraft",
            name="manufacturer_serial_number",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="airline",
            name="callsign",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="airline",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
