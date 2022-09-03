# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage  
@FileName       :   serializer.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:10
@Software       :   PyCharm
@Show           :
"""
from accounts.models import *
from exam_online.models import *
from rest_framework import serializers

# -------------------------------------------------------------------------------
# ---------------------------------Accounts--------------------------------------
# -------------------------------------------------------------------------------


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'is_staff', 'moblie', 'status', 'name']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'type']


class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'userid_id', 'roleid_id']
# -------------------------------------------------------------------------------
# ---------------------------------ExamOnline------------------------------------
# -------------------------------------------------------------------------------


class QuestionInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionInfo
        fields = ['id', 'name', 'mod_id', 'tq_type', 'type', 'is_share',
                  'user_id', 'updated_user_id', 'create_time', 'updated_time']


class OptionInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OptionInfo
        fields = ['id', 'questioninfo_id', 'option', 'option_content', 'is_right', 'create_time']


class ExaminationInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExaminationInfo
        fields = ['id', 'name', 'group_id', 'exam_type', 'create_user_id', 'create_time']


class ExaminationInfoQuestionInfoProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExaminationInfoQuestionInfoProfile
        fields = ['id', 'examination_id', 'question_id', 'user_id', 'input_content', 'is_right']
