# Generated by Django 3.0.7 on 2020-09-01 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_page', '0008_auto_20200617_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemenu',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 21, 20, 14, 185728), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='questionstatistics',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 21, 20, 14, 186728), verbose_name='添加时间'),
        ),
    ]
