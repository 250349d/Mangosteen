# Generated by Django 3.2 on 2025-01-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0020_alter_customuser_town_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, unique=True, verbose_name='名'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, unique=True, verbose_name='姓'),
        ),
    ]
