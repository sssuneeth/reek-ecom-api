# Generated by Django 4.1.4 on 2023-01-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reek', '0008_alter_itemsize_size_l_alter_itemsize_size_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsize',
            name='size_l',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='itemsize',
            name='size_m',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='itemsize',
            name='size_s',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
