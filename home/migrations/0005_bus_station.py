# Generated by Django 4.2 on 2023-05-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_bus_bus_type_bus_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='station',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
