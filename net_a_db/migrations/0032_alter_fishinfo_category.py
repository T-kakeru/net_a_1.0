# Generated by Django 4.1 on 2024-11-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0031_alter_fishinfo_fish_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'なし'), ('2', 'アロワナ'), ('3', 'ポリプテルス'), ('4', 'プレコ'), ('5', 'パクー（メチニスなど）'), ('6', 'カラシン(テトラなど)'), ('7', 'プラティ・卵生メダカなど'), ('8', 'ローチ'), ('9', 'エンゼルフィッシュ'), ('10', 'ディスカス'), ('11', 'シクリッド'), ('12', 'コリドラス'), ('13', '淡水エイ'), ('14', 'ベタ'), ('15', 'ナマズ'), ('16', 'フグ'), ('17', '川のエビ、貝、カニ'), ('18', '汽水魚'), ('19', 'その他熱帯魚'), ('20', 'メダカ'), ('21', '金魚'), ('22', '鯉'), ('23', '川魚'), ('24', 'その他淡水魚'), ('25', 'スズメダイ'), ('26', 'ヤッコ'), ('27', 'チョウチョウウオ'), ('28', 'ハギ'), ('29', 'ギンポ'), ('30', 'ベラ'), ('31', 'ハゼ'), ('32', 'ハタ'), ('33', 'フグ'), ('34', 'サメ、エイ'), ('35', 'タコ、イカ'), ('36', 'クラゲ、ナマコ、ヒトデなど'), ('37', '海のエビ、貝、カニ'), ('38', '一般に食用魚等の魚種'), ('39', 'その他海水魚')], max_length=20, null=True),
        ),
    ]
