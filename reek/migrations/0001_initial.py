# Generated by Django 4.1.4 on 2022-12-29 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('size_s', models.BooleanField(default=True)),
                ('size_m', models.BooleanField(default=True)),
                ('size_l', models.BooleanField(default=True)),
                ('real_price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reek.item')),
            ],
        ),
    ]
