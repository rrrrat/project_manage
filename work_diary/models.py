from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from accounts.models import Profile
from system_manager.models import Project

# Create your models here.


class diary(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, default=1)
    show = MDTextField()
    status = models.IntegerField(choices=((0, '未读'), (1, '已读')), default=0, verbose_name='状态')
    create_user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, default=1, related_name='create_user')
    receive_user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, default=1, related_name='receive_user')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "工作日记"
        verbose_name_plural = verbose_name
