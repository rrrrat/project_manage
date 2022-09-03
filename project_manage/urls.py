"""project_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question_manage/', include('question_manage.urls'), name='question_manage'),  # 问题管理
    path('accounts/', include('accounts.urls'), name='accounts'),  # 用户管理
    path('', include('project_page.urls')),  # 主页
    path('system_manager/', include('system_manager.urls')),  # 后台管理
    path('exam_online/', include('exam_online.urls')),  # 在线考试
    path('api/', include('api.urls')),  # api 预留
    url(r'mdeditor/', include('mdeditor.urls')),  # Markdown专用
    url(r'^api-auth/', include('rest_framework.urls')),  # api 专用
    url(r'^work_diary/', include('work_diary.urls')),  # api 专用
    path('password-reset/', include('password_reset.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)