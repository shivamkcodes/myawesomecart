# Generated by Django 3.0.2 on 2020-02-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(max_length=500),
        ),
    ]
