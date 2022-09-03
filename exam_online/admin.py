from django.contrib import admin
from exam_online.models import *

# Register your models here.

admin.site.register(QuestionInfo)
admin.site.register(OptionInfo)
admin.site.register(ExaminationInfo)
admin.site.register(ExaminationInfoQuestionInfoProfile)