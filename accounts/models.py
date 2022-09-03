# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   models.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   用户 Models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Profile(AbstractUser):
    """
    用户信息表
    """
    moblie = models.CharField(null=True, max_length=255, verbose_name="电话号码")
    status = models.CharField(null=True, max_length=255, default=1, verbose_name="状态")
    name = models.CharField(null=True, max_length=255, verbose_name="姓名")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Role(models.Model):
    """
    角色相关
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(null=True, max_length=255, verbose_name="名称")
    type = models.CharField(null=True, max_length=255, default=1, verbose_name="标签")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserRole(models.Model):
    """
    用户_角色关联
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    userid = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    roleid = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "用户_角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid
