# -*- coding:utf-8 -*-
# 生产配置

"""
Django settings for luffy project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#新增打包路径 因为我们的项目子应用目录进行了修改
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#h*07=+xz830-1v)7zl&05*3pxpjcv788z)k*)v01)=&hx$ko8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'home',
    'users',
    'xadmin',
    'crispy_forms',
    'reversion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'luffy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],#[os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luffy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'ceshi001',
        'PASSWORD': 'ceshi001',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }

}
#缓存
#缓存介质：文件/内存
#cdn 内容分发网络
CACHES = {
    "default":{
        "BACKEND":"django_redis.cache.RedisCache",
        "LOCATION":"redis://127.0.0.1:6379/0",
        "OPTIONS":{
            "CLIENT_CLASS":"django_redis.client.DefaultClient",
        }
    },
    # xadmin的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    #提供存储短信验证码
    "sms_code":{
            "BACKEND":"django_redis.cache.RedisCache",
            "LOCATION":"redis://127.0.0.1:6379/2",
            "OPTIONS":{
                "CLIENT_CLASS":"django_redis.client.DefaultClient",
            }
        }
}
#设置xadmin用户登录时session保存到redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]
MEDIA_ROOT = os.path.join(BASE_DIR,"uploads")
MEDIA_URL = "/media/"

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # },
        'file':{
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            # 日志位置文件名，必须手动创建
            'filename':os.path.join(os.path.dirname(BASE_DIR),"logs/luffy.log"),
            # 文件大小最大值300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量设置数量最大10
            'backupCount': 10,
            # 日志格式详细格式
            'formatter':'verbose',
        },
    },
    'loggers': {
        'django':{
            'handlers' : ['console','file'],
            'propagate' : True,
        },
        # 'django': {
        #     'handlers': ['console'],
        #     'propagate': True,  #
        # },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}
REST_FRAMEWORK ={
    #异常处理
    'EXCEPTION_HANDLER':'luffy.utils.exceptions.custom_exception_handler',
    #修改优先使用的登陆方式
    'DEFAULT_AUTHENTICATION_CLASS':(
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.BasicAuthentication',
        ''
    )
}
import datetime
#jwt字符串的有效期
JWT_AUTH ={
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=7),
    'JWT_RESPONSE_PAYLOAD_HANDLER':'users.utils.jwt_response_payload_handler'
}
#配置多条件登陆
AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend',
]

#配置让django的Auth模块调用users字应用下面的User数据模型类
AUTH_USER_MODEL = 'users.User'


#短信接口信息
SMS_ACCOUNTSID = "8aaf07086e0115bb016e683266493a2e"
SMS_ACCOUNTTOKEN = "76a4fe24f49d4899af097373c51ea9ba"
SMS_APPID = "8aaf07086e0115bb016e6832669f3a34"
SMS_SERVERIP = "sandboxapp.cloopen.com"