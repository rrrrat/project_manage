# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-20 13:04
@Software       :   PyCharm
@Show           :   在线考试 Urls
"""
from django.urls import path
from . import views

app_name = "exam_online"
urlpatterns = [
    path('questioninfo_manage/', views.questioninfo_manage, name="questioninfo_manage"),  # 试题列表
    path('get_questioninfo/', views.get_questioninfo, name="get_questioninfo"),  # 获取试题信息
    path('new_questioninfo/', views.new_questioninfo, name="new_questioninfo"),  # 新建试题
    path('edit_questioninfo/', views.edit_questioninfo, name='edit_questioninfo'),  # 编辑试题 q-211
    path('exam/', views.exam, name='exam'),  # 考试
    path('exam_list/', views.exam_list, name='exam_list'),  # 参加过的考试
    path('get_exam/', views.get_exam, name='get_exam'),  # 获取考试信息
    path('get_exam_info/', views.get_exam_info, name='get_exam_info'),  # 获取考试信息
]