# Generated by Django 4.1 on 2024-11-14 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0032_alter_fishinfo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishinfo',
            name='fish_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]