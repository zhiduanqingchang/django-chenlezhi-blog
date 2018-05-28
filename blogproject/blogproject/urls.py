"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# ChenHuan 2018/5/17 17:57 假如一个project中有多个app,用单一的方式来管理url可能会造成比较混乱的局面,
# 为了解决这个问题,我们可以用include的方法来配置url.
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    # ChenHuan 2018/5/17 17:58 其中namespace参数为我们指定了命名空间,
    # 这说明这个urls.py中的url是blog app下的,这样即使不同的app下有相同url也不会冲突了.
    # http://127.0.0.1:8000/blog/
    url(r'^simditor/', include('simditor.urls'))
    # ChenHuan 2018/5/19 10:02 django-simditor 一个 django 的富文本编辑器配置
]
