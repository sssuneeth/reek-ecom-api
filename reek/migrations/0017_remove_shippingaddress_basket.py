# Generated by Django 4.1.4 on 2023-01-17 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reek', '0016_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='basket',
        ),
    ]
