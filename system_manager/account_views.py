# Create your views here.
# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   account_views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   系统管理-Account-Views
"""
from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from django.contrib.auth.models import User, Group
import json
from accounts import models
from project_page.models import RoleMenu, PageMenu
"""
roles: 角色
groups: 用户组
users: 用户
"""
# Create your views here.

# -----------------------------------------------------------------------------------
# ---------------------------------------User----------------------------------------
# -----------------------------------------------------------------------------------


def user(request):
    """
    url: /system_manager/user/
    user视图
    :param request:
    :return:user.html
    """
    return render(request, 'system_manager/user.html', locals())


def get_user(request):
    """
    url: /system_manager/get_user/
    获取用户信息
    :param request:
    :return:Json-用户-Dict
    """
    user_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    username = request.GET.get('username', '')
    if username and username != '0':
        data['username'] = username

    users = models.Profile.objects.filter(**data).all()
    # 分页控制
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            user_data = {'id': users[i].id,
                         'username': users[i].username,
                         'name': users[i].name,
                         'email': users[i].email,
                         'last_login': users[i].last_login,
                         'moblie': users[i].moblie,
                         'createTime': users[i].date_joined}
            user_results.append(user_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': user_results, 'count': len(users)})


def user_edit(request):
    """
    url: /system_manager/user_edit/
    用户信息编辑
    :return: default-edit_user.html  |  Json-Status
    """
    if request.is_ajax():
        if request.POST:
            data = {}

            if request.POST['name']:
                name = request.POST['name']
            else:
                data['message'] = '请输入姓名！'
                return HttpResponse(json.dumps(data))

            if request.POST['email']:
                email = request.POST['email']
            else:
                data['message'] = '请输入邮箱！'
                return HttpResponse(json.dumps(data))

            if request.POST['moblie']:
                moblie = request.POST['moblie']
            else:
                data['message'] = '请输入手机号！'
                return HttpResponse(json.dumps(data))
            user_id = request.POST['id']
            group = request.POST['group']
            role = request.POST['role']
            user_info = models.Profile.objects.get(id=user_id)
            user_info.name = name
            user_info.email = email
            user_info.moblie = moblie
            user_info.save()
            user_info.groups.clear()
            user_info.groups.add(group)
            role_update = models.UserRole.objects.filter(userid_id=user_id).update(roleid_id=role)
            data['code'] = True
            data['msg'] = 'success'
            return HttpResponse(json.dumps(data))

    if request.GET.get('userId', ''):
        userId = request.GET.get('userId', '')
        user = models.Profile.objects.get(id=userId)
        user_group = user.groups.values().first()
        user_role = models.UserRole.objects.filter(userid_id=userId).first()
        roles = models.Role.objects.all()
        groups = Group.objects.all()
        return render(request, 'system_manager/edit_user.html', locals())

    return HttpResponse('SSS')


def add_user(request):
    """
    url: /system_manager/add_user/
    用户信息编辑
    :return: default-add_user.html  |  Json-Status
    """
    if request.is_ajax():
        if request.POST:
            data = {}
            if request.POST['username']:
                username = request.POST['username']
                if models.Profile.objects.filter(username=username):
                    data['message'] = '用户名已存在！请重新输入用户名！'
                    return HttpResponse(json.dumps(data))
            else:
                data['message'] = '请输入账户！'
                return HttpResponse(json.dumps(data))

            if request.POST['name']:
                name = request.POST['name']
            else:
                data['message'] = '请输入姓名！'
                return HttpResponse(json.dumps(data))

            if request.POST['email']:
                email = request.POST['email']
            else:
                data['message'] = '请输入邮箱！'
                return HttpResponse(json.dumps(data))

            if request.POST['moblie']:
                moblie = request.POST['moblie']
            else:
                data['message'] = '请输入手机号！'
                return HttpResponse(json.dumps(data))

            new_user = models.Profile.objects.create_user(name=name,
                                                          username=username,
                                                          email=email,
                                                          moblie=moblie,
                                                          password='000000')
            new_user.save()
            new_user.groups.add(request.POST['group'])
            user_id = models.Profile.objects.get(username=username).id
            role_add = models.UserRole(userid_id=user_id,
                                       roleid_id=request.POST['role'])
            role_add.save()
            return JsonResponse({'code':0,'msg':'success'})
    roles = models.Role.objects.all()
    groups = Group.objects.all()
    return render(request, 'system_manager/add_user.html', locals())


def user_remove(request):
    """
    url: /system_manager/user_remove/
    用户删除
    :param request:
    :return: Json-Status
    """
    if request.GET.get('userid', ''):
        user_id = request.GET.get('userid', '')
        models.Profile.objects.filter(id=user_id).delete()
        return JsonResponse({'success': True, 'msg': '删除成功！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})

# -----------------------------------------------------------------------------------
# ---------------------------------------group---------------------------------------
# -----------------------------------------------------------------------------------


def group(request):
    """
    url: /system_manager/group/
    用户组Views
    :param request:
    :return:default-group.html  |  Json-Status
    """
    if request.POST.get('name', ''):
        name = request.POST.get('name', '')
        id = request.POST.get('id', '')
        Group.objects.filter(id=id).update(name=name)
        return JsonResponse({'status': True})
    elif request.POST.get('addgroup', ''):
        addgroup = request.POST.get('addgroup', '')
        if Group.objects.filter(name=addgroup):
            return JsonResponse({'status': False, 'msg': '组名重复'})
        Group.objects.create(name=addgroup)
        return JsonResponse({'status': True})
    else:
        return render(request, 'system_manager/group.html', locals())


def get_group(request):
    """
    url: /system_manager/get_group/
    获取用户组信息
    :param request:
    :return:  Json-用户组-Dict
    """
    group_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    groups = Group.objects.filter(**data).all()

    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            group_data = {'id': groups[i].id,
                         'name': groups[i].name,}
            group_results.append(group_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': group_results, 'count': len(groups)})


def remove_group(request):
    """
    url: /system_manager/remove_group/
    删除用户组
    :param request:
    :return: Json-Status
    """
    if request.GET.get('groupid', ''):
        groupid = request.GET.get('groupid', '')
        Group.objects.filter(id=groupid).delete()
        return JsonResponse({'success': True, 'msg': '删除成功！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})

# -----------------------------------------------------------------------------------
# ---------------------------------------Role----------------------------------------
# -----------------------------------------------------------------------------------


def role(request):
    """
    url: /system_manager/role/
    角色列表
    :param request:
    :return:default-role.html  |  Json-Status
    """
    if request.POST.get('name', ''):
        name = request.POST.get('name', '')
        id = request.POST.get('id', '')
        models.Role.objects.filter(id=id).update(name=name)
        return JsonResponse({'status': True})
    elif request.POST.get('addrole', ''):
        addrole = request.POST.get('addrole', '')
        if models.Role.objects.filter(name=addrole):
            return JsonResponse({'status': False, 'msg': '角色名重复'})
        models.Role(name=addrole).save()
        return JsonResponse({'status': True})
    else:
        return render(request, 'system_manager/role.html', locals())


def get_role(request):
    """
    url: /system_manager/get_role/
    获取角色信息
    :param request:
    :return: Json-角色-Dict
    """
    role_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    roles = models.Role.objects.filter(**data).all()

    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            role_data = {'id': roles[i].id,
                         'name': roles[i].name,}
            role_results.append(role_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': role_results, 'count': len(roles)})


def remove_role(request):
    """
    url: /system_manager/remove_role/
    删除用户组
    :param request:
    :return: Json-Status
    """
    if request.GET.get('roleid', ''):
        roleid = request.GET.get('roleid', '')
        models.Role.objects.filter(id=roleid).delete()
        return JsonResponse({'success': True, 'msg': '删除成功！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})


def role_menu(request):
    """
    url: /system_manager/role_menu/
    用户菜单管理
    :param request:
    :return:default-role_menu.html  | Json-Status
    """
    if request.is_ajax():
        if request.POST:
            roleid = request.POST.get('roleid', '')
            menus = request.POST.get('menus', '')
            menus = eval(menus)
            try:
                RoleMenu.objects.filter(role=roleid).delete()
                for menu in menus:
                    role = models.Role.objects.get(id=roleid)
                    page_menu = PageMenu.objects.get(id=menu)
                    RoleMenu(role=role, page_menu=page_menu).save()
                data = {'code': 1}
                return HttpResponse(json.dumps(data))
            except:
                data = {'msg': '未知错误'}
                return HttpResponse(json.dumps(data))
    elif request.GET.get('roleid', ''):
        roleid = request.GET.get('roleid', '')
        page_menus = PageMenu.objects.all()
        system_manages = []
        system_manages.append({'title': '系统管理', 'id': 1})
        questions = []
        questions.append({'title': '工作空间', 'id': 3})
        exam_onlines = []
        exam_onlines.append({'title': '在线考试', 'id': 17})
        word_diarys = []
        word_diarys.append({'title': '工作日记', 'id': 21})
        for page_menu in page_menus:
            if page_menu.pid == '1':
                system_manages.append({'title': page_menu.title, 'id': page_menu.id})
            elif page_menu.pid == '3':
                questions.append({'title': page_menu.title, 'id': page_menu.id})
            elif page_menu.pid == '17':
                exam_onlines.append({'title': page_menu.title, 'id': page_menu.id})
            elif page_menu.pid == '21':
                word_diarys.append({'title': page_menu.title, 'id': page_menu.id})

        role_menus = RoleMenu.objects.values_list('page_menu', flat=True).filter(role=roleid).all()
        return render(request, 'system_manager/role_menu.html', locals())
    else:
        return HttpResponse('非法请求！')