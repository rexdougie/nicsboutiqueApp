# Generated by Django 3.1.3 on 2020-11-10 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutiqueApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='designer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boutiqueApp.designer'),
        ),
    ]