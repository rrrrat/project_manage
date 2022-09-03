# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   项目主页 Views
"""
from django.shortcuts import render, HttpResponse
import datetime
from django_redis import get_redis_connection
from question_manage.models import Question
from accounts.models import UserRole
from django.utils import timezone
import json
from . import models
from .bullshit import generator
# Create your views here.


def index(request):
    return render(request, 'index.html', locals())


def get_menu(request):
    """
    url: /project_page/get_menu/
    获取菜单
    :param request:
    :return: Json-菜单-List
    """
    data = []
    if request.user.is_anonymous:
        # 从数据库内获取未登录用户所能访问的菜单
        menu = models.PageMenu.objects.get(id=3)  # 顶级菜单
        menu_p = models.PageMenu.objects.get(id=10)  # 二级菜单
        # 顶级菜单
        menu_data = {'id': menu.id,
                     'title': menu.title,
                     'icon': menu.icon,
                     'type': int(menu.type),
                     'href': menu.href,
                     'spread': menu.spread}
        # 顶级菜单加入二级菜单
        menu_p_data = [{'id': menu_p.id,
                           'title': menu_p.title,
                           'icon': menu_p.icon,
                           'type': int(menu_p.type),
                           'openType': menu_p.opentype,
                           'href': menu_p.href,
                           'spread': menu_p.spread}]
        menu_data['children'] = menu_p_data
        data.append(menu_data)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        # 从数据库内获取当前用户角色所能访问的菜单
        rid = UserRole.objects.get(userid_id=request.user.id).roleid_id  # 获取用户角色
        menus = models.RoleMenu.objects.filter(role_id=rid).all()  # 获取角色所属菜单
        for menu in menus:
            menu_pid = menu.page_menu.pid
            if menu_pid == '0':  # menu_pid为0则为顶级菜单
                menu_data = {'id': menu.page_menu.id,
                             'title': menu.page_menu.title,
                             'icon': menu.page_menu.icon,
                             'type': int(menu.page_menu.type),
                             'href': menu.page_menu.href,
                             'spread': menu.page_menu.spread}
                menus_p = models.RoleMenu.objects.filter(role_id=rid).all()  # 获取角色所属菜单
                meun_p_data = []
                for menu_p in menus_p:
                    menu_p_type = menu_p.page_menu.type  # 获取角色二级菜单
                    if menu_p_type == '1'  and str(menu_p.page_menu.pid) == str(menu.page_menu.id):
                        menu_p_data = {'id': menu_p.page_menu.id,
                                       'title': menu_p.page_menu.title,
                                       'icon': menu_p.page_menu.icon,
                                       'type': int(menu_p.page_menu.type),
                                       'openType': menu_p.page_menu.opentype,
                                       'href': menu_p.page_menu.href,
                                       'spread': menu_p.page_menu.spread}
                        meun_p_data.append(menu_p_data)
                    menu_data['children'] = meun_p_data
                data.append(menu_data)
        return HttpResponse(json.dumps(data), content_type='application/json')


def get_notice(request):
    """
    url: /project_page/get_notice/
    获取用户消息
    :param request:
    :return: Json-消息-List
    """
    if request.user.is_anonymous:
        msg = [{'id': 1, 'title': '消息'},{'id': 2, 'title': '提示'},{'id': 1, 'title': '通知'}]
        return HttpResponse(json.dumps(msg), content_type='application/json')
    else:
        conn = get_redis_connection('default')  # 获取消息列表，Redis
        infos_id = conn.smembers(request.user.username)
        children = []

        for info_id in infos_id:
            question = Question.objects.get(id=info_id)
            notice = {'id': int(info_id), 'title': question.name,
                      'time': question.createtime.strftime( '%Y-%m-%d %H:%M:%S'),
                      'avatar': '/static/admin/images/success.png'}
            children.append(notice)
        msg = [{'id': 1, 'title': '消息', 'children': children},
               {'id': 2, 'title': '提示'},
               {'id': 3, 'title': '通知'}]
        return HttpResponse(json.dumps(msg), content_type='application/json')


def console(request):
    """
    url: /project_page/console/
    控制台
    :param request:
    :return: console.html
    """
    current_user = request.user
    all_question = Question.objects.filter(user=current_user).all()  # 获取所有问题
    unresolved = Question.objects.filter(status=0, user=current_user).all()  # 获取状态为未解决的问题
    solved = Question.objects.filter(status=2, user=current_user).all()  # 获取状态为已解决的问题
    cur_time = datetime.datetime.now()
    day_num = cur_time.isoweekday()
    week_day = (cur_time - datetime.timedelta(days=day_num))
    week_question = Question.objects.filter(createtime__range=(week_day, cur_time), user=current_user).all()
    mon_question = Question.objects.filter(createtime__month=cur_time.month, user=current_user).all()
    day_question = Question.objects.filter(createtime__day=cur_time.day, user=current_user).all()
    top_questions = Question.objects.filter(status=0, user=current_user).order_by('-id')[:8]
    news_question = Question.objects.filter(createtime__day=cur_time.day, user=current_user).all()
    solveds_question = Question.objects.filter(successtime__day=cur_time.day, user=current_user).all()
    unresolveds_question = Question.objects.filter(status=0, user=current_user).all()
    new_tables = []
    unresolved_tables = []
    solved_tables = []
    week_questions = models.QuestionStatistics.objects.filter(createtime__range=(week_day, cur_time)).all()
    for weeks_question in week_questions:
        new_tables.append(weeks_question.new)
        unresolved_tables.append(weeks_question.unresolved)
        solved_tables.append(weeks_question.solved)
    # 你可以打破常识， 但不能没有常识  --日本寺院 / code? line? id?/
    new_tables.append(len(news_question))
    unresolved_tables.append(len(unresolveds_question))
    solved_tables.append(len(solveds_question))
    return render(request, 'console.html', locals())


def day_flash(request):
    """
    url: /project_page/day_flash/
    每日数据写入
    :param request:
    :return: Status
    """
    cur_time = datetime.datetime.now()
    new_question = Question.objects.filter(createtime__day=cur_time.day).all()
    solved_question = Question.objects.filter(successtime__day=cur_time.day).all()
    unresolved_question = Question.objects.filter(status=0).all()
    print(cur_time.day)
    if models.QuestionStatistics.objects.filter(createtime__year=cur_time.year, createtime__month=cur_time.month,
                                                createtime__day=cur_time.day):
        return HttpResponse('Have Data!')
    models.QuestionStatistics(new=len(new_question),
                              solved=len(solved_question),
                              unresolved=len(unresolved_question),
                              createtime=timezone.now()).save()
    return HttpResponse('OK!')


def bulshit(request):
    """
    url: /project_page/bulshit/
    这个东西不重要
    :param request:
    :return: new_question.html
    """
    if request.GET:
        title = request.GET['title']
        x = generator(title)
    return render(request, 'new_question.html', locals())
