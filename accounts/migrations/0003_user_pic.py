# Generated by Django 4.1.4 on 2023-01-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='default_images/user.png', upload_to='profile_pics'),
        ),
    ]
