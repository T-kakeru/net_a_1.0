# Generated by Django 4.1 on 2024-11-14 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0033_fishinfo_fish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='location',
            field=models.CharField(blank=True, choices=[('1', '自宅'), ('2', 'ペットショップ'), ('3', '水族館・展示'), ('4', 'その他')], max_length=20, null=True),
        ),
    ]
