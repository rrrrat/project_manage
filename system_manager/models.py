# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   models.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   系统管理 Models
"""
from django.db import models
from django.utils import timezone
from accounts.models import Profile, Role
# Create your models here.


class Mod(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name="模块名称")
    show = models.CharField(max_length=500, verbose_name="模块说明")
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "模块"
        verbose_name_plural = verbose_name


class PlatForm(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name="平台名称")
    show = models.CharField(max_length=500, verbose_name="平台说明")
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "平台"
        verbose_name_plural = verbose_name


class Project(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name="项目名称")
    show = models.CharField(max_length=500, verbose_name="项目说明")
    platform = models.ForeignKey(PlatForm, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='平台')
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='负责人')
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='角色')
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name


