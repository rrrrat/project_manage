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

from django import template
from exam_online import models
from django.utils.safestring import mark_safe
from time import strftime, localtime

register = template.Library()


@register.filter
def get_option(questioninfo_id):
    """
    获取选项
    :param questioninfo_id: 试题ID
    :return: 选项
    """
    x = models.OptionInfo.objects.filter(questioninfo_id=questioninfo_id).all
    print(x)
    return x
