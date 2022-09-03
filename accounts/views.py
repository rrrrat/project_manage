# Create your views here.
# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
# 故乡今夜思千里，霜鬓明朝又一年  --《除夜作》  / 810 / ;  第一题猜到答案了么？umm，没思路么？ -- 答案: 5
@Project        :   project_manage
@FileName       :   views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   用户相关 Views
"""
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from .models import Profile
import json
from accounts import models


def sign_up(request):
    """
    用户注册
    """
    if request.user.is_authenticated:
        return redirect('/')
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

            if request.POST['password']:
                password = request.POST['password']
            else:
                data['message'] = '请输入密码！'
                return HttpResponse(json.dumps(data))

            if request.POST['moblie']:
                moblie = request.POST['moblie']
            else:
                data['message'] = '请输入手机号！'
                return HttpResponse(json.dumps(data))

            new_user = models.Profile.objects.create_user(name=name,
                                                          username=username,
                                                          email=email,
                                                          password=password,
                                                          moblie=moblie)
            new_user.save()
            new_user.groups.add(1)
            models.UserRole(userid_id=new_user.id, roleid_id=2).save()
            user = authenticate(username=username, password=password)
            login(request, user)
            data['status'] = 1
            return HttpResponse(json.dumps(data))

    return render(request, 'accounts/sign_up.html', locals())


def sign_in(request):
    """
    用户登录
    """
    if request.user.is_authenticated:
        return redirect('/')
    name = "用户登录"
    if request.is_ajax():
        if request.POST:
            data = {}
            if request.POST['username']:
                username = request.POST['username']
            else:
                data['message'] = '请输入用户名！'
                return HttpResponse(json.dumps(data))

            if request.POST['password']:
                password = request.POST['password']
            else:
                data['message'] = '请输入密码！'
                return HttpResponse(json.dumps(data))

            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                data['status'] = 1
                return HttpResponse(json.dumps(data))
            except Exception as Error:
                data['message'] = '用户名或密码错误！'
                return HttpResponse(json.dumps(data))

    return render(request, 'accounts/sign_in.html', locals())


def edit_userinfo(request):
    """
    用户编辑
    :param request:
    :return:
    """
    if request.is_ajax():
        if request.POST:
            try:
                name = request.POST.get('name', '')
                if name == "":
                    return JsonResponse({'msg': '请输入姓名'})
                mobile = request.POST.get('mobile', '')
                if mobile == "":
                    return JsonResponse({'msg': '请输入手机号'})
                email = request.POST.get('email', '')
                if email == "":
                    return JsonResponse({'msg': '请输入email'})
                user_info = Profile.objects.get(id=request.user.id)
                user_info.name = name
                user_info.moblie = mobile
                user_info.email = email
                user_info.save()
                return JsonResponse({'status': True})
            except:
                return JsonResponse({'msg': '未知错误'})
        else:
            return JsonResponse({'msg': '未知错误'})
    else:
        return HttpResponse('???')


def sign_out(request):
    """
    用户退出
    """
    logout(request)
    return redirect('/')
