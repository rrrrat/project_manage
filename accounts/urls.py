# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   用户 Urls
-- 第一题开始喽，各位小伙伴们，锻炼一下自己的逻辑思维能力吧！
-- accounts, exam_online, project_page, question_manage, system_manager, templates
"""
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.sign_up, name="register"),  # 用户注册
    path('logout/', views.sign_out, name="logout"),  # 用户登出
    path('login/', views.sign_in, name='login'),  # 用户登录
    path('edit_userinfo/', views.edit_userinfo, name='edit_userinfo')  # 编辑用户信息 q-153
]