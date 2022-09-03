# ProjectManage
2020年的了，这个如果有人觉得不错，请告诉我，我继续维护。
基于Django的项目管理系统，可实现对项目实施过程中出现的问题进行上报，跟踪，管理。

[![](https://img.shields.io/badge/Python-3.6+-green.svg)]()[![](https://img.shields.io/badge/Django-3.0.7-green.svg)]()[![](https://img.shields.io/badge/Version-0.50-green.svg)]()

# 当前实现功能

```
1. 系统管理
2. 问题管理
3. 在线考试
```

# 部署

1. 要求： Python3.6+，MySQL， Redis

2. 依赖:   ```pip3 install -r requirements.txt```

3. 配置：

```python
修改 project_manage/settings.py
1. 修改数据库连接
# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_manage',  # 数据库名
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '2030916',  # 数据库密码
        'HOST': '47.94.111.124',  # 数据库地址
        'PORT': '3306',  # 数据库端口
    },
}
# Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",  # redis连接地址
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "密码",  # redis密码，若无密码则注释
            "DECODE_RESPONSES":True
        }
    },
}
2. 修改邮件发送
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  # TLS协议， 不用管
EMAIL_HOST = 'smtp.qq.com'  # SMTP地址
EMAIL_PORT = 587  # 邮箱端口
EMAIL_HOST_USER = '843636329@qq.com'  # 邮箱账号
EMAIL_HOST_PASSWORD = '***'  # 邮箱密码（QQ之类的邮箱需在设置内申请）
DEFAULT_FROM_EMAIL = '843636329@qq.com'  # 默认发送邮件地址
```

4. 启动： ```python manage.py runserver 0.0.0.0:8080```

# 演示站

目前没了

# 目录结构

```bash
.
├── Makefile  
├── Readme.md  # 本文件目录
├── accounts  # 用户管理
├── api  # 接口（预留，当前未启动）
├── exam_online  # 在线考试
├── project_manage  # 设置
├── project_page  # 主页
├── question_manage  # 问题管理
├── source
├── static  # 模板元素
├── system_manager  # 系统管理
├── templates  # 模板
├── uploads  # 文件上传地址
├── manage.py  # 主程序
├── requirements.txt  # requirements
```


