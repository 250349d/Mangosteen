# Generated by Django 3.2 on 2024-12-31 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0011_auto_20241231_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='other_adress',
            field=models.CharField(blank=True, error_messages={'unique': 'この番地、マンション名は既に使用されています。'}, help_text='150文字以内。日本語のみ使用可能です。', max_length=150, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='番地、マンション名には日本語、アルファベット、数字、記号(@, ., +, -, _)のみ使用できます。', regex='^[\\u4E00-\\u9FFF\\u3040-\\u309F\\u30A0-\\u30FF\\uFF00-\\uFFEFa-zA-Z0-9@.+-_]+$')], verbose_name='番地、マンション名'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='town_area',
            field=models.CharField(blank=True, error_messages={'unique': 'この町域は既に使用されています。'}, help_text='150文字以内。日本語のみ使用可能です。', max_length=150, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='町域には日本語、アルファベット、数字、記号(@, ., +, -, _)のみ使用できます。', regex='^[\\u4E00-\\u9FFF\\u3040-\\u309F\\u30A0-\\u30FF\\uFF00-\\uFFEFa-zA-Z0-9@.+-_]+$')], verbose_name='町域'),
        ),
    ]
