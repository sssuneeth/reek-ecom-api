# Generated by Django 4.1.4 on 2022-12-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reek', '0006_alter_item_rating_alter_itemimage_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rocking_now',
            field=models.BooleanField(default=False),
        ),
    ]
