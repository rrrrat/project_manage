# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   models.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-20 13:04
@Software       :   PyCharm
@Show           :   在线考试 Models
"""
from django.db import models
from django.utils import timezone
from system_manager.models import Mod
from accounts.models import Profile
from django.contrib.auth.models import Group


# 试题信息
class QuestionInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=500, default='', verbose_name='试题题目')
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, verbose_name='所属模块', default='')
    tq_type = models.IntegerField(
        choices=((0, '选择'), (1, '判断'), (2, '填空')), verbose_name='试题类型', default=0
    )
    type = models.IntegerField(
        choices=((0, '基础类'), (1, '业务类'), (2, '技术类'),
                 (3, '沟通类'), (4, '综合类'), (5, '其他')), verbose_name='类型', default=0
    )
    is_share = models.BooleanField(default=False, verbose_name='是否分享')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cuser', verbose_name='创建人')
    updated_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='uuser', verbose_name='更新人')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '试题信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OptionInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    questioninfo = models.ForeignKey(QuestionInfo, on_delete=models.CASCADE, verbose_name='试题信息')
    option = models.IntegerField(choices=((0, 'A'), (1, 'B'),
                                          (2, 'C'), (3, 'D'),
                                          (4, 'E'), (5, 'F')), default=0, verbose_name='选项')
    option_content = models.CharField(max_length=255, default='', verbose_name='选项内容')
    is_right = models.BooleanField(default=True, verbose_name='是否为正确答案')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '试题选项信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.option_content


class ExaminationInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, default='', verbose_name='考试名称')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='所属用户组')
    exam_type = models.IntegerField(choices=((0, '练习'), (1, '正式')), default=0, verbose_name='类型')
    create_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='考试人')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ExaminationInfoQuestionInfoProfile(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    examination = models.ForeignKey(ExaminationInfo, on_delete=models.CASCADE, verbose_name='考试信息')
    question = models.ForeignKey(QuestionInfo, on_delete=models.CASCADE, verbose_name='试题信息')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='用户信息')
    input_content = models.CharField(max_length=5000, default='', verbose_name='考试名称')
    is_right = models.BooleanField(default=True, verbose_name='是否为正确')

    class Meta:
        verbose_name = '考试_试题_用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.input_content

