# Generated by Django 3.0.3 on 2020-05-21 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manager', '0002_auto_20200521_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 39, 0, 740712), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 39, 0, 741043), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 39, 0, 741412), verbose_name='添加时间'),
        ),
    ]