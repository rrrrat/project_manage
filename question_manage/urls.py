# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   问题管理 Url
-- 准备好了么？这题可能有点难
"""
from django.urls import path
from . import views


app_name = "question_manage"
urlpatterns = [
    path('new_question/', views.new_question, name='new_question'),  # 新建问题
    path('question/', views.question, name='question'),  # 问题查看
    path('get_question/', views.get_question, name='get_question'),  # 获取问题(JSON)
    path('views_question/', views.views_question, name='views_question'),  # 显示问题具体内容
    path('solved_question/', views.solved_question, name='solved_question'),  # 已完结问题
    path('unresolved_question/', views.unresolved_question, name='unresolved_question'),  # 未完结问题
    path('change_user/', views.change_user, name='change_user'),  # 改变负责人
    path('team_question/', views.team_question, name='team_question'),
    path('get_team_question/', views.get_team_question, name='get_team_question'),
    # update_log
    path('update_log/', views.update_log, name='update_log'),  # 更新记录
    path('test/', views.test, name='test')  # 常驻 q-271
]