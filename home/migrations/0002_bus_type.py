# Generated by Django 4.2 on 2023-05-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]