# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   models.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   项目主页 Models
"""
from django.db import models
from django.utils import timezone
from accounts.models import Role

# Create your models here.


class PageMenu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=20, verbose_name="名称")
    icon = models.CharField(max_length=50, verbose_name="图标")
    type = models.CharField(max_length=25, verbose_name="标签")
    pid = models.CharField(max_length=25, verbose_name="上级ID")
    opentype = models.CharField(max_length=30, verbose_name="openType", default='_iframe')
    href = models.CharField(max_length=90, null=True, verbose_name="href")
    spread = models.CharField(null=True, max_length=20, verbose_name="spread")
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class RoleMenu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    page_menu = models.ForeignKey(PageMenu, blank=True, null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "角色_菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.page_menu


class QuestionStatistics(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    new = models.IntegerField(default=0, verbose_name='新问题')
    solved = models.IntegerField(default=0, verbose_name='已解决问题')
    unresolved = models.IntegerField(default=0, verbose_name='待解决问题')
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "问题统计"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[{}, {}, {}]'.format(self.new, self.solved, self.unresolved)