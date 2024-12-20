# Generated by Django 4.1 on 2024-10-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0023_alter_fishinfo_food_alter_fishinfo_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishinfo',
            name='age',
            field=models.CharField(blank=True, choices=[('1', '１ヵ月未満'), ('2', '１～３ヵ月'), ('3', '３～６ヵ月'), ('3', '６～１２ヵ月'), ('3', '１年以上'), ('3', '２年以上'), ('3', '３年以上'), ('3', '５年以上'), ('3', '７年以上'), ('3', '１０年以上')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fishinfo',
            name='location',
            field=models.CharField(blank=True, choices=[('1', '自宅'), ('2', 'ペットショップ'), ('3', '水族館'), ('3', 'その他')], max_length=20, null=True),
        ),
    ]
