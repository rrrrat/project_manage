# Generated by Django 3.0.3 on 2020-06-17 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_page', '0007_auto_20200616_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemenu',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 11, 5, 42, 644668), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='questionstatistics',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 11, 5, 42, 646143), verbose_name='添加时间'),
        ),
    ]
