# Generated by Django 4.1 on 2024-10-31 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0026_fishinfo_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fishinfo',
            name='test',
        ),
    ]
