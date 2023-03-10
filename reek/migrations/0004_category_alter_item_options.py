# Generated by Django 4.1.4 on 2022-12-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reek', '0003_rename_itemsizes_itemsize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-id']},
        ),
    ]
