# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   问题管理 Views
"""
from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from django.utils import timezone
from .models import Question
from .utils import Email
from django_redis import get_redis_connection
from system_manager.models import Mod, Project
from accounts.models import Profile
from django.contrib.auth.models import User, Group
import json
# Create your views here.
"""
dept: 部门
deptid: 部门ID
indexno: 指标号
docno: 单据号
qname: 姓名
qphone: 电话
user: 用户
mod: 模块
project: 项目
show: 内容
"""


def question(request):
    """
    url: /question_manage/question/
    问题信息
    :param request:
    :return:question.html
    """
    if Group.objects.get(user=request.user.id).id != 2:
        disabled = 'disabled'
    users = Profile.objects.all()
    mods = Mod.objects.all()
    projects = Project.objects.all()
    return render(request, 'question_manage/question.html', locals())


def solved_question(request):
    """
    url: /question_manage/solved_question/
    已解决问题
    :param request:
    :return:solved_question.html
    """

    mods = Mod.objects.all()
    projects = Project.objects.all()
    return render(request, 'question_manage/solved_question.html', locals())


def unresolved_question(request):
    """
    url: /question_manage/unresolved_question/
    待解决问题
    :param request:
    :return:default-unresolved_question.html  |  Json-status
    """
    if request.POST:
        # 解决问题
        try:
            successinfo = request.POST.get('successinfo', '')
            id = request.POST.get('id', '')
            # 更新状态
            Question.objects.filter(id=id).update(successinfo=successinfo, status=2, successtime=timezone.now())
            question_name =Question.objects.get(id=id)
            # url = request.META['HTTP_HOST']  # 获取当前url
            # email = Email(request.user.email)
            # email.send_question_over(question_name.name, request.user.name, id, successinfo, url)  # 发送邮件
            return JsonResponse({'status': True})
        except:
            return JsonResponse({'msg': '未知错误'})

    users = Profile.objects.all()
    mods = Mod.objects.all()
    projects = Project.objects.all()
    return render(request, 'question_manage/unresolved_question.html', locals())


def get_question(request):
    """
    url: /question_manage/solved_question/
    获取问题
    :param request:
    :return:Json-问题-List
    """
    question_results = []
    # 按名字搜索
    data = {}
    user = request.user.id
    if Group.objects.get(user=user).id != 2:
        data['user'] = user

    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    userin = request.GET.get('user', '')
    if userin and userin != '0':
        data['user'] = userin

    mod = request.GET.get('mod', '')
    if mod and mod != '0':
        data['mod'] = mod

    project = request.GET.get('project', '')
    if project and project != '0':
        data['project'] = project

    status = request.GET.get('status', '')
    if status and status != '1':
        data['status'] = status

    deptid = request.GET.get('deptid', '')
    if deptid:
        data['deptid__contains'] = deptid

    indexno = request.GET.get('indexno', '')
    if indexno:
        data['indexno__contains'] = indexno

    docno = request.GET.get('docno', '')
    if docno:
        data['docno__contains'] = docno

    qname = request.GET.get('qname', '')
    if qname:
        data['qname__contains'] = qname

    qphone = request.GET.get('qphone', '')
    if qphone:
        data['qphone__contains'] = qphone


    questions = Question.objects.filter(**data).all()
    # 分页控制
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            question_data = {'id': questions[i].id,
                             'name': questions[i].name,
                             'dept': questions[i].dept,
                             'project': questions[i].project.name,
                             'mod': questions[i].mod.name,
                             'deptid': questions[i].deptid,
                             'indexno': questions[i].indexno,
                             'docno': questions[i].docno,
                             'qname': questions[i].qname,
                             'qphone': questions[i].qphone,
                             'status': '待反馈' if questions[i].status == 0 else '已解决',
                             'createtime': questions[i].createtime}
            question_results.append(question_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': question_results, 'count': len(questions)})


def new_question(request):
    """
    url: /question_manage/new_question/
    问题新建
    :param request:
    :return: default-new_question.html  |  Json-Status
    """
    if request.is_ajax():
        # 新建问题
        if request.POST:
            data = {}
            if request.POST['name']:
                name = request.POST['name']
            else:
                data['message'] = '请输入问题名！'
                return HttpResponse(json.dumps(data))
            try:
                dept = request.POST['dept']
                deptid = request.POST.get('deptid', '')
                indexno = request.POST.get('indexno', '')
                docno = request.POST.get('docno', '')
                qname = request.POST.get('qname', '')
                qphone = request.POST.get('qphone', '')
                user = request.POST['user']  # 无异常处理，若未填写则无返回
                mod = request.POST['mod']  # ...
                project = request.POST['project']  # ...
                show = request.POST['show']  # 无异常处理，若未填写则无返回
                project = Project.objects.get(id=project)
                mod = Mod.objects.get(id=mod)
                user = Profile.objects.get(username=user)
                x = Question(name=name, dept=dept, user=user,
                             project=project, mod=mod, show=show,
                             deptid=deptid, indexno=indexno, docno=docno,
                             qname=qname, qphone=qphone, createtime=timezone.now())
                x.save()
            except:
                data['message'] = '问题创建失败！请联系管理员解决！'
                return HttpResponse(json.dumps(data))
            try:
                conn = get_redis_connection('default')
                conn.sadd(request.POST['user'], x.id)
            except:
                data['message'] = '问题已创建成功，但Redis访问出现错误！'
                return HttpResponse(json.dumps(data))
            # try:
            #     url = request.META['HTTP_HOST']
            #     email = Email(user.email)
            #     email.send_new_question(name, user.name, x.id, url)  # 发送邮件
            # except:
            #     data['message'] = '问题已创建成功，但Email发送出现错误！'
            #     return HttpResponse(json.dumps(data))
            data['status'] = 1
            return HttpResponse(json.dumps(data))
    users = Profile.objects.all()
    mods = Mod.objects.all()
    projects = Project.objects.all()
    # 你现在的生活也许不是你想要的，但绝对是你自找的!  / 271?214?136?height?=?  | result < 1300/
    return render(request, 'question_manage/new_question.html', locals())


def views_question(request):
    """
    url: /question_manage/views_question/
    问题内容展示
    :param request:
    :return: views_question.html
    """
    id = request.GET.get('questionId', '')
    try:
        conn = get_redis_connection('default')
        conn.srem(request.user.username, id)  # 问题已查看从redis内删除
    except:
        pass
    question = Question.objects.get(id=int(id))
    return render(request, 'question_manage/views_question.html', locals())


def change_user(request):
    """
    url: /question_manage/change_user/
    :param request:
    :return: Json-Status
    """
    question_id = request.POST.get('id', '')
    change_user_id = request.POST.get('userid', '')
    user = request.user
    user_group = Group.objects.get(user=user).id
    if Question.objects.filter(id=question_id, user=user) is not None or user_group == 2:
        Question.objects.filter(id=question_id).update(user_id=change_user_id)
        return JsonResponse({'status': '0'})
    else:
        return JsonResponse({'msg': '禁止越权访问'})


def team_question(request):
    """
    url: /question_manage/team_question/
    团队进度
    :param request:
    :return:team_question.html
    """
    return render(request, 'question_manage/team_question.html', locals())


def get_team_question(request):
    """

    :param request:
    :return:
    """
    users = Profile.objects.all()
    cur_time = timezone.datetime.now()
    day_num = cur_time.isoweekday()
    week_day = (cur_time - timezone.timedelta(days=day_num))
    team_question_result = []
    for user in users:
        reusult = {'id': str(user.id),
                   'name': str(user.name),
                   'allquestionlen': len(Question.objects.filter(user=user.id).all()),
                   'unresolvedlen': len(Question.objects.filter(status=0, user=user.id).all()),
                   'solved': len(Question.objects.filter(status=2, user=user.id).all()),
                   'weekquestionlen': len(Question.objects.filter(createtime__range=(week_day, cur_time),
                                                                    user=user.id).all()),
                   'monquestion': len(Question.objects.filter(createtime__month=cur_time.month, user=user.id).all()),
                   'dayquestion': len(Question.objects.filter(createtime__day=cur_time.day, user=user.id).all())}
        team_question_result.append(reusult)
    return JsonResponse({'code': 0, 'data': team_question_result, 'count': len(team_question_result)})

def update_log(request):
    """
    url: /question_manage/update_log/
    更新记录
    :param request:
    :return:update_log.html
    """
    update_log = Question.objects.get(id=1)
    return render(request, 'question_manage/update_log.html', locals())


def test(request):
    x = get_redis_connection('default')
    return HttpResponse('ok')
