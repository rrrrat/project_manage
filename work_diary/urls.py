# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   工作日记 Url
"""

from django.urls import path
from . import views


app_name = "work_diary"
urlpatterns = [
    path('new_diary/', views.new_diary, name='new_diary'),  # 新建问题
    path('my_diary/', views.my_diary, name='my_diary'),  # 问题查看
    path('get_diary/', views.get_diary, name='get_diary'),  # 获取问题(JSON)
    path('view_diary/', views.view_diary, name='view_diary'),  # 显示问题具体内容
    path('receive_diary/', views.receive_diary, name='receive_diary'),  # 已完结问题
]