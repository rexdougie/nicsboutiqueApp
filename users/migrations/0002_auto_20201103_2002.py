# Generated by Django 3.1.3 on 2020-11-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='Profile-Pics'),
        ),
    ]