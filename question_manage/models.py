# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   models.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   问题管理 Models
"""
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField #必须导入
from accounts.models import Profile
from system_manager.models import Project, Mod

# Create your models here.


class Question(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name="问题名")
    dept = models.CharField(max_length=255, null=True, verbose_name="部门")
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, default=1)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, default=1)
    mod = models.ForeignKey(Mod, blank=True, null=True, on_delete=models.SET_NULL, default=1)
    show = MDTextField()
    deptid = models.CharField(default=0, max_length=255, null=True, verbose_name='单位编码')
    indexno = models.CharField(default=0, max_length=255, null=True, verbose_name='指标号')
    docno = models.CharField(default=0, max_length=25, null=True, verbose_name='单据号')
    qname = models.CharField(default=0, max_length=255, null=True, verbose_name="姓名")
    qphone = models.CharField(default=0, max_length=255, null=True, verbose_name='电话')
    status = models.IntegerField(choices=((0, '待反馈'), (1, '待解决'), (2, '已解决')), default=0, verbose_name='状态')
    successinfo = models.CharField(null=True, max_length=255, verbose_name="完成信息")
    successtime = models.DateTimeField(null=True, verbose_name="完成时间")
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = verbose_name


class QuestionStatistics(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    new = models.IntegerField(default=0, verbose_name='新问题')
    solved = models.IntegerField(default=0, verbose_name='已解决问题')
    unresolved = models.IntegerField(default=0, verbose_name='待解决问题')
    createtime = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")
