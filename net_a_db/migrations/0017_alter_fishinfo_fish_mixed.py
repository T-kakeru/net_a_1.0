# Generated by Django 4.1 on 2024-03-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0016_alter_fishinfo_aquarium_size_alter_fishinfo_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='fish_mixed',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
