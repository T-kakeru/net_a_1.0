# Generated by Django 4.1 on 2024-03-10 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0005_icon_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishinfo',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='upload_img/'),
        ),
    ]