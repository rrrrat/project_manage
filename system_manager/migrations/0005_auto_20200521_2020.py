# Generated by Django 3.0.3 on 2020-05-21 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manager', '0004_auto_20200521_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 20, 20, 54, 952638), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 20, 20, 54, 952981), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 20, 20, 54, 953348), verbose_name='添加时间'),
        ),
    ]
