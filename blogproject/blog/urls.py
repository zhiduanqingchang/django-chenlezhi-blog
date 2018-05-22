#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 17:32
# @Author  : ChenHuan
# @Site    : 
# @File    : urls.py
# @Desc    : 应用blog的URLconf(就像是 Django 所支撑网站的目录,它的本质是URL模式以及要为该URL模式调用的视图函数之间的映射表)
# @Software: PyCharm

from django.conf.urls import url
from blog import views
# ChenHuan 2018/5/17 17:34 从应用中引入views模块,或者从模块(在Python的import语法中,blog/views.py 转译为 blog.views )中引入相应视图.
# Python 搜索路径:Python搜索路径,就是使用import语句时,Python所查找的系统目录清单.

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ChenHuan 2018/5/17 17:46 这是URLpattern,他是一个Python元组,元组中第一个元素是模式匹配字符串(正则表达式);
    # 第二个元素是那个模式将使用的视图函数;另外我们还传递了另外一个参数 name,这个参数的值将作为处理函数 index 的别名,这在以后会用到.
    # 简单来说,我们只是告诉 Django,所有指向 URL / 的请求都应由index这个视图函数来处理.

    url(r'^detail/(?P<article_slug>[\w\-]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    # ChenHuan 2018/5/18 15:35 定义文章详情页面url,正则表达式r'^detail/(?P<article_slug>[\w\-]+)/$匹配时会调用view.ArticleDetailView类视图
    # 即detail/和后面的/之间的字符串,并把它作为参数article_slug传递给views.ArticleDetailView.as_view()参数

    url(r'^categories/$', views.CategoryView.as_view(), name='categories'),
    # ChenHuan 2018/5/21 8:26 文章分类页面
    url(r'^category/(?P<category_slug>[\w\-]+)/$', views.CategoryArticleView.as_view(), name='category'),
    # ChenHuan 2018/5/21 8:26 文章分类详情

    url(r'^archives/$', views.ArchiveView.as_view(), name='archives'),
    # ChenHuan 2018/5/21 8:27 文章归档
]
# ChenHuan 2018/5/17 17:36 urlpatterns用于绑定网址和处理函数的对应关系