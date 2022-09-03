# Create your views here.
# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   project_views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   系统管理-Project-Views
"""
from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from system_manager.models import Project, Mod, PlatForm
from project_page.models import PageMenu
"""
Projects: 项目
mods: 模块
platforms: 平台
menus: 菜单
"""
# -----------------------------------------------------------------------------------
# ---------------------------------------Project---------------------------------------
# -----------------------------------------------------------------------------------
def project(request):
    """
    url: /system_manager/project/
    项目基础Views
    :param request:
    :return:project.html
    """
    return render(request, 'system_manager/project.html', locals())


def get_project(request):
    """
    url: /system_manager/get_project/
    获取项目信息
    :param request:
    :return:Json-项目-Dict
    """
    project_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    projects = Project.objects.filter(**data).all()
    # 分页控制
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            project_data = {'id': projects[i].id,
                            'name': projects[i].name,
                            'show': projects[i].show,
                            'platform': projects[i].platform.name,
                            'staff': projects[i].user.name,
                            'createtime': projects[i].createtime}
            project_results.append(project_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': project_results, 'count': len(projects)})


def remove_project(request):
    """
    url: /system_manager/remove_project/
    删除项目
    :param request:
    :return:Json-Status
    """
    if request.GET.get('projectid', ''):
        projectid = request.GET.get('projectid', '')
        # Project.objects.filter(id=projectid).delete()
        return JsonResponse({'success': False, 'msg': '就一个项目了，先别删了，大哥！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})


def add_project(request):
    """
    添加账户
    :param request:
    :return:
    """
    return HttpResponse('功能正在开发中')


def edit_project(request):
    """
    添加账户
    :param request:
    :return:
    """
    return HttpResponse('功能正在开发中')


# -----------------------------------------------------------------------------------
# ---------------------------------------mod---------------------------------------
# -----------------------------------------------------------------------------------


def mod(request):
    """
    url: /system_manager/mod/
    :param request:
    :return:default-mod.html  |  Json-Status
    """
    if request.POST.get('name', ''):
        name = request.POST.get('name', '')
        show = request.POST.get('show', '')
        id = request.POST.get('id', '')
        Mod.objects.filter(id=id).update(name=name, show=show)
        return JsonResponse({'status': True})
    elif request.POST.get('addmod', ''):
        addmod = request.POST.get('addmod', '')
        show = request.POST.get('modshow', '')
        if Mod.objects.filter(name=addmod):
            return JsonResponse({'status': False, 'msg': '模块名重复'})
        Mod(name=addmod, show=show).save()
        return JsonResponse({'status': True})
    else:
        return render(request, 'system_manager/mod.html', locals())


def get_mod(request):
    """
    url: /system_manager/get_mod/
    获取用户信息
    :param request:
    :return:Json-模块-Dict
    """
    mod_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    mods = Mod.objects.filter(**data).all()

    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            mod_data = {'id': mods[i].id,
                        'name': mods[i].name,
                        'show': mods[i].show,
                        'createtime': mods[i].createtime}
            mod_results.append(mod_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': mod_results, 'count': len(mods)})


def remove_mod(request):
    """
    url: /system_manager/remove_mod/
    删除用户组
    :param request:
    :return: Json-Status
    """
    if request.GET.get('modid', ''):
        modid = request.GET.get('modid', '')
        Mod.objects.filter(id=modid).delete()
        return JsonResponse({'success': True, 'msg': '删除成功！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})


# -----------------------------------------------------------------------------------
# ---------------------------------------platform------------------------------------
# -----------------------------------------------------------------------------------


def platform(request):
    """
    url: /system_manager/platform/
    平台基础Views
    :param request:
    :return:default-platform.html  |  Json-Status
    """
    if request.POST.get('name', ''):
        name = request.POST.get('name', '')
        show = request.POST.get('show', '')
        id = request.POST.get('id', '')
        PlatForm.objects.filter(id=id).update(name=name, show=show)
        return JsonResponse({'status': True})
    elif request.POST.get('addplatform', ''):
        addplatform = request.POST.get('addplatform', '')
        show = request.POST.get('platformshow', '')
        if PlatForm.objects.filter(name=addplatform):
            return JsonResponse({'status': False, 'msg': '平台名重复'})
        PlatForm(name=addplatform, show=show).save()
        return JsonResponse({'status': True})
    else:
        return render(request, 'system_manager/platform.html', locals())


def get_platform(request):
    """
    url: /system_manager/get_platform/
    获取平台信息
    :param request:
    :return: Json-平台-Dict
    """
    platform_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    platforms = PlatForm.objects.filter(**data).all()

    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            platform_data = {'id': platforms[i].id,
                             'name': platforms[i].name,
                             'show': platforms[i].show,
                             'createtime': platforms[i].createtime}
            platform_results.append(platform_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': platform_results, 'count': len(platforms)})


def remove_platform(request):
    """
    url: /system_manager/remove_platform/
    删除平台
    :param request:
    :return: Json-Status
    """
    if request.GET.get('platformid', ''):
        platformid = request.GET.get('platformid', '')
        PlatForm.objects.filter(id=platformid).delete()
        return JsonResponse({'success': True, 'msg': '删除成功！'})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})


# -----------------------------------------------------------------------------------
# ---------------------------------------menu----------------------------------------
# -----------------------------------------------------------------------------------


def menu(request):
    """
    url: /system_manager/menu/
    菜单基础Views
    :param request:
    :return:defalut-menu.html  |  Json-Status
    """
    if request.POST.get('name', ''):
        name = request.POST.get('name', '')
        show = request.POST.get('show', '')
        id = request.POST.get('id', '')
        PageMenu.objects.filter(id=id).update(name=name, show=show)
        return JsonResponse({'status': True})
    elif request.POST.get('addplatform', ''):
        addplatform = request.POST.get('addplatform', '')
        show = request.POST.get('platformshow', '')
        if PageMenu.objects.filter(name=addplatform):
            return JsonResponse({'status': False, 'msg': '模块名重复'})
        PageMenu(name=addplatform, show=show).save()
        return JsonResponse({'status': True})
    else:
        return render(request, 'system_manager/menu.html', locals())


def get_menu(request):
    """
    url: /system_manager/get_menu/
    获取菜单信息
    :param request:
    :return:Json-菜单-Dict
    """
    menu_results = []
    data = {}
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name

    menus = PageMenu.objects.filter(**data).all()

    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit
    for i in range(min_page, max_page):
        try:
            menu_data = {'id': menus[i].id,
                         'title': menus[i].title,
                         'icon': menus[i].icon,
                         'type': menus[i].type,
                         'pid':menus[i].pid,
                         'opentype':menus[i].opentype,
                         'href': menus[i].href,
                         'spread': menus[i].spread}
            menu_results.append(menu_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': menu_results, 'count': len(menus)})


def remove_menu(request):
    """
    url: /system_manager/remove_menu/
    删除菜单
    :param request:
    :return:Json-Status
    """
    if request.GET.get('pagemenuid', ''):
        pagemenuid = request.GET.get('pagemenuid', '')
        # PageMenu.objects.filter(id=platformid).delete()
        return JsonResponse({'success': True, 'msg': pagemenuid})
    else:
        return JsonResponse({'success': False, 'msg': '删除失败！'})
