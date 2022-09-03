from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from .models import diary
from django.utils import timezone
from accounts.models import Profile
from system_manager.models import Project
import json

# Create your views here.

def my_diary(request):
    """
    url: /question_manage/question/
    问题信息
    :param request:
    :return:question.html
    """
    users = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'work_diary/my_diary.html', locals())


def receive_diary(request):
    """
    url: /question_manage/question/
    问题信息
    :param request:
    :return:question.html
    """
    users = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'work_diary/receive_diary.html', locals())


def new_diary(request):
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
            try:
                receive_user = request.POST['receive_user']  # 无异常处理，若未填写则无返回
                project = request.POST['project']  # ...
                show = request.POST['show']  # 无异常处理，若未填写则无返回
                project = Project.objects.get(id=project)
                receive_user = Profile.objects.get(username=receive_user)
                create_user = request.user
                x = diary(project=project, show=show, receive_user=receive_user, create_user=create_user,
                          create_time=timezone.now())
                x.save()
                data['status'] = 1
            except:
                data['message'] = '问题创建失败！请联系管理员解决！'
                return HttpResponse(json.dumps(data))
            return HttpResponse(json.dumps(data))
    users = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'work_diary/new_diary.html', locals())


def get_diary(request):
    """
    url: /question_manage/solved_question/
    获取问题
    :param request:
    :return:Json-问题-List
    """
    diary_results = []
    # 按名字搜索
    data = {}
    if request.GET.get('type', '') == '1':
        data['receive_user'] = request.user.id
    else:
        data['create_user'] = request.user.id

    project = request.GET.get('project', '')
    if project and project != '0':
        data['project'] = project

    status = request.GET.get('status', '')
    if status and status != '2':
        data['status'] = status

    receive_user = request.GET.get('receiveuser', '')
    if receive_user and receive_user != '0':
        data['receive_user'] = receive_user

    create_user = request.GET.get('createuser', '')
    if create_user and create_user != '0':
        data['create_user'] = create_user

    diarys = diary.objects.filter(**data).all()
    # 分页控制
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            diarys_data = {'id': diarys[i].id,
                           'project': diarys[i].project.name,
                           'status': '未读' if diarys[i].status == 0 else '已读',
                           'receiveuser': diarys[i].receive_user.name,
                           'createuser': diarys[i].create_user.name,
                           'createtime': diarys[i].create_time,}
            diary_results.append(diarys_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': diary_results, 'count': len(diarys)})


def view_diary(request):
    """
    url: /question_manage/views_question/
    问题内容展示
    :param request:
    :return: views_question.html
    """
    id = request.GET.get('diaryId', '')
    diary_views = diary.objects.get(id=int(id))
    if request.user.id == diary_views.receive_user.id:
        diary_views.status = 1
        diary_views.save()
    return render(request, 'work_diary/views_diary.html', locals())