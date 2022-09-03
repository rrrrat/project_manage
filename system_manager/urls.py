# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   系统管理Urls
"""
from django.urls import path
from . import account_views, project_views

app_name = "system_manager"
urlpatterns = [
    # -------------------------------------------------------------------
    # account change
    # user
    path('get_user/', account_views.get_user, name='get_user'),
    path('user/', account_views.user, name="user"),
    path('user_edit/', account_views.user_edit, name='user_edit'),
    path('user_remove/', account_views.user_remove, name='user_remove'),
    path('add_user/', account_views.add_user, name='add_user'),
    # group
    path('group/', account_views.group, name='group'),
    path('get_group/', account_views.get_group, name='get_group'),
    path('remove_group/', account_views.remove_group, name='remove_group'),
    # role
    path('role/', account_views.role, name='role'),
    path('get_role/', account_views.get_role, name='get_role'),
    path('remove_role/', account_views.remove_role, name='remove_role'),
    path('role_menu/', account_views.role_menu, name='role_menu'),
    # -------------------------------------------------------------------
    # project change
    # project
    path('project/', project_views.project, name='project'),
    path('get_project/', project_views.get_project, name='get_project'),
    path('remove_project/', project_views.remove_project, name='remove_project'),
    path('add_project/', project_views.add_project, name='add_project'),
    path('edit_project/', project_views.edit_project, name='edit_project'),
    # mod
    path('mod/', project_views.mod, name='mod'),
    path('get_mod/', project_views.get_mod, name='get_mod'),
    path('remove_mod/', project_views.remove_mod, name='remove_mod'),
    # platform
    path('platform/', project_views.platform, name='platform'),
    path('get_platform/', project_views.get_platform, name='get_platform'),
    path('remove_platform/', project_views.remove_platform, name='remove_platform'),
    # menu
    path('menu/', project_views.menu, name='menu'),
    path('get_menu/', project_views.get_menu, name='get_menu'),
    path('remove_menu/', project_views.remove_menu, name='remove_menu'),
]