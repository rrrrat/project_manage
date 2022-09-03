# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   项目主页 Urls
"""
from django.urls import path
from . import views, utils_upload_img
app_name = "project_page"
urlpatterns = [
    path('', views.index, name='index'),
    path('get_menu/', views.get_menu, name='get_menu'),  # 获取菜单
    path('get_notice/', views.get_notice, name='get_notice'),  # 获取消息
    path('upload_img/', utils_upload_img.upload_img, name='upload_img'),  # 上传图片
    path('console/', views.console, name='console'),  # 控制台
    path('day_flash/', views.day_flash, name='day_flash'),  # 定期调用函数，统计每日已解决问题
    path('bulshit/', views.bulshit, name='bulshit')  # 写着玩的，v-182
]