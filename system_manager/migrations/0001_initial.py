# Generated by Django 3.0.3 on 2020-05-21 15:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='模块名称')),
                ('show', models.CharField(max_length=500, verbose_name='模块说明')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 24, 55, 229393), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '模块',
                'verbose_name_plural': '模块',
            },
        ),
        migrations.CreateModel(
            name='PlatForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='平台名称')),
                ('show', models.CharField(max_length=500, verbose_name='平台说明')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 24, 55, 229822), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '平台',
                'verbose_name_plural': '平台',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('show', models.CharField(max_length=500, verbose_name='项目说明')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2020, 5, 21, 15, 24, 55, 230272), verbose_name='添加时间')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system_manager.PlatForm', verbose_name='平台')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Role', verbose_name='角色')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
    ]
