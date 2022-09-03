# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage  
@FileName       :   exam_online_utils.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-29 13:03
@Software       :   PyCharm
@Show           :   在线考试 Utils
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_manage.settings')
django.setup()
from django import template
from exam_online import models
import random


register = template.Library()


@register.filter
def get_option(questioninfo_id):
    """
    获取选项
    :param questioninfo_id: 试题ID
    :return: 选项
    """
    results = []
    x = models.OptionInfo.objects.filter(questioninfo_id=questioninfo_id).all()
    # options = ['A', 'B', 'C', 'D', 'E', 'F']
    x = list(x)
    random.shuffle(x)
    for i in x:
        data = {'option': i.option, 'option_content': i.option_content, 'option_value': i.option}
        results.append(data)

    return results


@register.filter
def get_range(value):
    """
    range实现
    :param value: 数
    :return: range实列
    """
    return range(1, value)
