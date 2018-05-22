"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# ChenHuan 2018/5/17 18:06 项目的绝对路径 os.path.abspath(file)返回一个文件在当前环境中的绝对路径,
# 这里file 一参数,os.path.dirname(__file__)返回当前python执行脚本的执行路径(看下面的例子),
# 这里__file__为固定参数
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5(=&a7b#8q9*87-08_jox&vxe2qjbn2e29hy0p6(%7o@!l4qp2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 为了安全起见，在生产环境下需要关闭 DEBUG 选项以及设置允许访问的域名
ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.chenlezhi.com']
# ALLOWED_HOSTS 是允许访问的域名列表,127.0.0.1 和 localhost 是本地访问的域名,.chenlezhi.com 是访问服务器的域名.
# 域名前加一个点表示允许访问该域名下的子域名,比如 www.chenlezhi.com、test.chenlezhi.com 等二级域名同样允许访问.如果不加前面的点则只允许访问 chenlezhi.com.

# Application definition

# ChenHuan 2018/5/17 15:37 INSTALLED_APPS是一个一元数组.
# 里面是应用中要加载的自带或者自己定制的app包路径列表
INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    # 'simditor',
    # ChenHuan 2018/5/19 10:04 django-simditor 一个 django 的富文本编辑器配置
    'pygments',
]

# ChenHuan 2018/5/17 17:05 web应用中需要加载的一些中间件列表,是一个一元数组,
# 里面是django自带的或者定制的中间件包路径.MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ChenHuan 2018/5/17 17:06 一个字符串,表示你的根 URLconf 的模块名;
# 当访问url的时候,Django会根据ROOT_URLCONF的设置来装载URLConf,然后按顺序逐个匹配URLConf里的URLpatterns,
# 如果找到则会调用相关联的视图函数,并把HttpRequest对象作为第一个参数(通常是request).
ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ChenHuan 2018/5/17 18:08 DIRS 就是设置模板的路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# ChenHuan 2018/5/17 17:07 Django运行所需配置;
# Django会先根据settings中的 WSGI_APPLICATION 来获取handler;
# 在创建project的时候,Django会默认创建一个wsgi.py文件,而settings中的WSGI_APPLICATION配置也会默认指向这个文件.
WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# ChenHuan 2018/5/17 17:09 Python 内置的 SQLite3 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# ChenHuan 2018/5/17 15:26 表示默认语言的一个字符串,必须是标准语言格式
# ChenHuan 2018/5/17 15:27 LANGUAGE_CODE = 'en-us'

# ChenHuan 2018/5/17 15:26 设置后台管理语言为简体中文
LANGUAGE_CODE = 'zh-Hans'

# ChenHuan 2018/5/17 15:31 把国际时区改为中国时区
# ChenHuan 2018/5/17 15:31 TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

# ChenHuan 2018/5/17 15:28 国际化:是指为了该软件在任何地区的潜在使用而进行程序设计的过程.
# 它包括了为将来翻译而标记的文本（比如用户界面要素和错误信息等）、日期和时间的抽象显示以便保证不同地区的标准得到遵循、为不同时区提供支持,并且一般确保代码中不会存在关于使用者所在地区的假设.
# 您会经常看到国际化被缩写为“I18N”(18表示Internationlization这个单词首字母I和结尾字母N之间的字母有18个).
USE_I18N = True

# ChenHuan 2018/5/17 15:30 本地化:是指使一个国际化的程序为了在某个特定地区使用而进行实际翻译的过程.
# 有时,本地化缩写为L10N .
USE_L10N = True

# ChenHuan 2018/5/17 15:30 开启Django的时区功能
USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
# ChenHuan 2018/5/22 17:55 suit在admin里设置时间的一个小bug,需要把时间格式指定一下.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# ChenHuan 2018/5/17 22:52 表示映射到静态文件的url
STATIC_URL = '/static/'

# ChenHuan 2018/5/17 22:53 静态文件绝对路径
STATIC_PATH = os.path.join(BASE_DIR, 'blog/static')
# ChenHuan 2018/5/17 22:54 表示是一个列表,放各个app的static目录及公共的static目录
STATICFILES_DIRS = (
    STATIC_PATH,
)

# ChenHuan 2018/5/17 22:55 另一种设置 STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# ChenHuan 2018/5/17 22:58 媒体文件信息配置
MEDIA_URL = "/media/"
# ChenHuan 2018/5/17 23:03 定义了基地址
MEDIA_ROOT = os.path.join(BASE_DIR, "blog/media")
CKEDITOR_UPLOAD_PATH = "images"

# ChenHuan 2018/5/19 10:04 django-simditor 一个 django 的富文本编辑器配置
# SIMDITOR_UPLOAD_PATH = 'uploads/'
# SIMDITOR_IMAGE_BACKEND = 'pillow'
#
# SIMDITOR_TOOLBAR = [
#     'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
#     'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
#     'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
#     'markdown', 'emoji'
# ]
#
# SIMDITOR_CONFIGS = {
#     'toolbar': SIMDITOR_TOOLBAR,
#     'upload': {
#         'url': '/simditor/upload/',
#         'fileKey': 'upload'
#     },
#     'emoji': {
#         'imagePath': '/static/simditor/images/emoji/'
#     }
# }

SUIT_CONFIG = {
    # ChenHuan 2018/5/22 17:58 suit页面配置
    'ADMIN_NAME': '倦了请直说-博客',
    # ChenHuan 2018/5/22 17:58 登录界面提示
    'LIST_PER_PAGE': 20,
    'MENU': ({'label': u'文章', 'app': 'blog', 'models': ('blog.Article',)},
             {'label': u'分类', 'app': 'blog', 'models': ('blog.Category',)},
             {'label': u'语录', 'app': 'blog', 'models': ('blog.Ana',)},
             # ChenHuan 2018/5/22 18:01 每一个字典表示左侧菜单的一栏
             # {'label': u'SQL管理', 'app': 'web_sso', 'models': ('web_sso.Sql', 'web_sso.PreSql', 'web_sso.Direction')},
             # 可以是多个字典
             ),
    # ChenHuan 2018/5/22 18:00 label表示name,app表示上边的install的app，models表示用了哪些models
}