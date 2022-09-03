# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
# 人生有两个悲剧: 第一是想得到的得不到，第二是想得到的得到了  --王尔德  / zpz /  所见即所得？ No！;
@FileName       :   views.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-20 13:04
@Software       :   PyCharm
@Show           :   在线考试 Views
"""
import random
import hashlib

from django.shortcuts import render, HttpResponse
from exam_online import models
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from system_manager.models import Mod
from django.utils import timezone
# Create your views here.
"""
options: 选项
questioninfo_tq_types: 试题类型
questioninfo_types: 类型
mods: 模块
"""


def questioninfo_manage(request):
    """
    url: /exam_online/questioninfo_manage/
    问题管理
    :param request:
    :return: questioninfo_manage.html
    """
    return render(request, 'exam_online/questioninfo_manage.html', locals())


def get_questioninfo(request):
    """
    url: /exam_online/get_questioninfo/
    获取考题列表
    :param request:
    :return:Json-考题-Dict
    """
    questioninfo_results = []
    data = {}
    # 按名字搜索
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name
    # 创建用户搜索
    creat_user = request.GET.get('user', '')
    if creat_user and creat_user != '0':
        data['creat_user'] = creat_user
    # 按模块搜索
    mod = request.GET.get('mod', '')
    if mod and mod != '0':
        data['mod'] = mod
    # 按试题类型搜索
    tq_type = request.GET.get('type', '')
    if tq_type and tq_type != '0':
        data['tq_type'] = tq_type

    questioninfos = models.QuestionInfo.objects.filter(**data).all()
    # 分页
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit - 1
    for i in range(min_page, max_page):

        try:
            question_data = model_to_dict(questioninfos[i])  # questioninfos：试题信息集合
            questioninfo_results.append(question_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': questioninfo_results, 'count': len(questioninfos)})


def new_questioninfo(request):
    """
    url: /exam_online/new_questioninfo/
    添加考题
    :param request:
    :return:default-new_question.html  ｜  Json-Status
    """
    if request.is_ajax():
        if request.POST:
            options = {}
            data = {'user': request.user, 'updated_user': request.user}
            name = request.POST.get('name', '')
            mod = request.POST.get('mod', '')
            tq_type = request.POST.get('tq_type', '')
            q_type = request.POST.get('type', '')
            option = request.POST.get('option', '')
            A = request.POST.get('0', '')  # 试题 A
            B = request.POST.get('1', '')  # ...
            C = request.POST.get('2', '')  # ...
            D = request.POST.get('3', '')  # ...
            E = request.POST.get('4', '')  # ...
            F = request.POST.get('5', '')  # 答案 F

            if name:
                data['name'] = name
            else:
                return JsonResponse({'msg':'请输入试题题目'}, safe=False)

            if mod and mod != '-1':
                data['mod'] = Mod.objects.get(id=mod)
            else:
                return JsonResponse({'msg':'请选择模块'}, safe=False)

            if tq_type and tq_type != '-1':
                data['tq_type'] = tq_type
            else:
                return JsonResponse({'msg':'请选择试题类型'}, safe=False)

            if q_type and q_type != '-1':
                data['type'] = q_type
            else:
                return JsonResponse({'msg':'请选择类型'}, safe=False)

            if option and option != '-1':
                option = option
            else:
                return JsonResponse({'msg':'请选择正确答案'}, safe=False)
            # 答案塞入'options'
            if A:
                options['0'] = A
            if B:
                options['1'] = B
            if C:
                options['2'] = C
            if D:
                options['3'] = D
            if E:
                options['4'] = E
            if F:
                options['5'] = F
            # 检测正确答案是否为空
            if option not in options.keys():
                return JsonResponse({'msg':'正确答案为必填项'}, safe=False)

            questioninfo_db = models.QuestionInfo(**data)  # 基本试题信息存入QuestionInfo
            questioninfo_db.save()

            for option_info in options:
                # option_info: 答案信息   --此处可优化，等个大神
                if option_info == option:  # 若为正确答案则 is_right为True
                    models.OptionInfo(option_content=options[option_info],
                                      option=option_info,
                                      questioninfo=questioninfo_db,
                                      is_right=True).save()
                else:
                    models.OptionInfo(option_content=options[option_info],
                                      option=option_info,
                                      questioninfo=questioninfo_db,
                                      is_right=False).save()
            return JsonResponse({'status': 1}, safe=False)

    options = models.OptionInfo.option.field.choices
    questioninfo_tq_types = models.QuestionInfo.tq_type.field.choices
    questioninfo_types = models.QuestionInfo.type.field.choices
    mods = Mod.objects.all()
    return render(request, 'exam_online/new_question.html', locals())


def edit_questioninfo(request):
    """
    url: /exam_online/edit_questioninfo/
    :param request:
    :return:default-edit_question.html  |  Json-Status
    """
    if request.GET:
        options = models.OptionInfo.option.field.choices
        questioninfo_tq_types = models.QuestionInfo.tq_type.field.choices
        questioninfo_types = models.QuestionInfo.type.field.choices
        mods = Mod.objects.all()
        question_id = request.GET.get('id', '')
        questioninfo = models.QuestionInfo.objects.get(id=question_id)  # 通过id搜索试题
        options_info = models.OptionInfo.objects.filter(questioninfo_id=question_id)  # 通过试题id搜索相关选项
        option_info_true = models.OptionInfo.objects.get(questioninfo_id=question_id, is_right=True)  # 获取正确答案
        return render(request, 'exam_online/edit_question.html', locals())

    elif request.POST:
        questioninfo_id = request.POST.get('questioninfo_id', '')
        name = request.POST.get('name', '')
        mod = request.POST.get('mod', '')
        tq_type = request.POST.get('tq_type', '')
        q_type = request.POST.get('type', '')
        option = request.POST.get('option', '')
        questioninfo_data = {'name': name, 'mod': mod, 'tq_type': int(tq_type), 'type': int(q_type),
                             'updated_user': request.user}
        models.QuestionInfo.objects.filter(id=questioninfo_id).update(**questioninfo_data)  # 更新试题信息
        for i in range(0, 5):
            # 更新选项信息
            try:
                option_op = request.POST.get(str(i), '')
                models.OptionInfo.objects.filter(option=i,
                                                 questioninfo_id=questioninfo_id
                                                 ).update(option_content=option_op)
            except:
                break
        return JsonResponse({'status': '0'})

    else:
        return HttpResponse('错误请求')


def exam(request):
    """
    url: /exam_online/exam/
    考试
    :param request:
    :return:default-exam.html  |  Json-分数-Int
    """
    if request.POST:
        score = 0
        exam_name = request.POST.get('exam_name', '')
        exam_type = request.POST.get('exam_type', '')
        # 创建考试信息
        examination_info = models.ExaminationInfo(name=exam_name,
                                                  exam_type=exam_type,
                                                  group_id=4,
                                                  create_user=request.user)
        examination_info.save()
        for questioninfo_option in request.POST:
            questioninfo_id, option = questioninfo_option, request.POST[questioninfo_option]  # 构建questioninfo_id，option
            if questioninfo_id == 'exam_type':
                # 垃圾代码 又不能没有 那就留着呗
                continue
            elif questioninfo_id == 'exam_name':
                # 垃圾代码 又不能没有 那就留着呗
                continue
            # 从题库中取出 is_right
            result = models.OptionInfo.objects.filter(questioninfo_id=questioninfo_id, option=option).values('is_right')
            # select is_right from OptionInfo where questioninfo_id = 1 and option = 1
            # True False
            # 判断是否为正确答案
            if result[0]['is_right'] is True:
                # 若为正确答案则 ExaminationInfoQuestionInfoProfile-is_right 为 True
                score += 1
                models.ExaminationInfoQuestionInfoProfile(examination=examination_info,
                                                          question_id=questioninfo_id,
                                                          user=request.user,
                                                          input_content=exam_name,
                                                          is_right=True).save()
            else:
                # 反之
                models.ExaminationInfoQuestionInfoProfile(examination=examination_info,
                                                          question_id=questioninfo_id,
                                                          user=request.user,
                                                          input_content=exam_name,
                                                          is_right=False).save()
        return JsonResponse({'msg': score})
    questioninfos = random.sample(list(models.QuestionInfo.objects.all()), 20)
    data = timezone.now().strftime('%Y%m%d%H%M%S')
    b = data.encode(encoding='utf-8')
    m = hashlib.md5()
    m.update(b)
    str_md5 = m.hexdigest()
    print(str_md5.upper())
    return render(request, 'exam_online/exam.html', locals())


def exam_list(request):
    """
    url: /exam_online/exam_list/
    问题管理
    :param request:
    :return: exam_list.html
    """
    return render(request, 'exam_online/exam_list.html', locals())


def get_exam(request):
    """
    url: /exam_online/get_exam/
    获取考题列表
    :param request:
    :return:Json-考题-Dict
    """
    exam_results = []
    data = {}
    # 按名字搜索
    data['create_user'] = request.user
    name = request.GET.get('name', '')
    if name:
        data['name__contains'] = name
    # 按类型搜索
    xtype = request.GET.get('type', '')
    if xtype:
        data['exam_type'] = xtype

    exams = models.ExaminationInfo.objects.filter(**data).all()
    # 分页
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', '')
    page = int(page)
    limit = int(limit)
    min_page = page * limit - limit
    max_page = page * limit - 1
    for i in range(min_page, max_page):
        try:
            exam_data = model_to_dict(exams[i])  # exam_data：试题信息集合
            exam_results.append(exam_data)
        except:
            pass
    return JsonResponse({'code':0, 'data': exam_results, 'count': len(exams)})


def get_exam_info(request):
    """
    url: /exam_online/get_exam_info/
    考试
    :param request:
    :return:default-exam.html  |  Json-分数-Int
    """
    if request.GET:
        exam_id = request.GET.get('examid', '')
        exam_id = int(exam_id)
        exam_infos = models.ExaminationInfoQuestionInfoProfile.objects.filter(examination=exam_id).all()
    return render(request, 'exam_online/get_exam_info.html', locals())
