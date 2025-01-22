# Generated by Django 5.1.4 on 2025-01-21 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_group', models.CharField(editable=False, help_text='0: 注文者, 1: 配達員', max_length=1, verbose_name='送信者の属性')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='メッセージ送信時間')),
                ('text', models.CharField(max_length=150, verbose_name='メッセージ文')),
                ('read_flag', models.BooleanField(default=False)),
                ('task', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='client_app.task', verbose_name='チャット')),
            ],
        ),
    ]
