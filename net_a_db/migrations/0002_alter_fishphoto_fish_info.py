# Generated by Django 4.1 on 2024-03-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishphoto',
            name='fish_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='net_a_db.fishinfo'),
        ),
    ]
