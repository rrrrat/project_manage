# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
# author:tangchaolizi
# datetime:2020-05-19 14:05
# software:PyCharm
from .models import QuestionStatistics
from question_manage.models import Question
import datetime


def day_flash():
    print('run')
    cur_time = datetime.datetime.now()
    new_question = Question.objects.filter(createtime__day=cur_time.day).all()
    solved_question = Question.objects.filter(successtime__day=cur_time.day).all()
    unresolved_question = Question.objects.filter(status=0).all()
    QuestionStatistics(new=len(new_question),
                       solved_question=len(solved_question),
                       unresolved_question=len(unresolved_question)).save()
    return 0