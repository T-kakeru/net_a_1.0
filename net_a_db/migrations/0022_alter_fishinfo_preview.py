# Generated by Django 4.1 on 2024-03-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0021_alter_fishinfo_aquarium_size_alter_fishinfo_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='preview',
            field=models.ImageField(upload_to='upload_img/'),
        ),
    ]
