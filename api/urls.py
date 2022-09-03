# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage  
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :
"""
from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'role', RoleViewSet)
router.register(r'userrole', UserRoleViewSet)
router.register(r'questioninfo', QuestionInfoViewSet)
router.register(r'optioninfo', OptionInfoViewSet)
router.register(r'examinationinfo', ExaminationInfoViewSet)
router.register(r'examinationinfoquestioninfoprofile', ExaminationInfoQuestionInfoProfileViewSet)

app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls)),
]