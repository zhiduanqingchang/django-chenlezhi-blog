#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 17:49
# @Author  : ChenHuan
# @Site    :
# @File    : views.py
# @Desc    : views.py文件包含了页面的业务逻辑
# @Software: PyCharm

import markdown2
# from django.utils.text import slugify
# import markdown
# ChenHuan 2018/5/19 8:56 Markdown 的渲染器就能够把我们写的文章转换为标准的 HTML 文档
from django.shortcuts import render, get_object_or_404
# ChenHuan 2018/5/17 17:51 render方法的作用:结合一个给定的模板和一个给定的字典,并返回一个渲染后的HttpResponse对象.
# 通俗来讲,就是把content的内容,加载进templates中定义的文件,并通过浏览器渲染展现.
# from django.http import HttpResponse
from blog.models import Article, Category, Ana
from django.views.generic import ListView, DetailView, FormView
from django.db.models.aggregates import Count
# ChenHuan 2018/5/21 0:09 Count 计算分类下的文章数

# def index(request):
#     """ ChenHuan 2018/5/17 17:55
#     函数体现了这个过程:它首先接受了一个名为 request 的参数,这个 request 就是 Django 为我们封装好的 HTTP 请求,它是类 HttpRequest 的一个实例.
#     然后我们便直接返回了一个 HTTP 响应给用户,这个 HTTP 响应也是 Django 帮我们封装好的,它是类 HttpResponse 的一个实例,只是我们给它传了一个自定义的字符串参数.
#     """
#     # return HttpResponse('欢迎访问博客首页')
#     # return render(request, 'blog/index.html', context={
#     #     'title' : '博客首页',
#     #     'welcome' : '欢迎访问博客首页',
#     # })
#     articles = Article.objects.all().order_by('-created_time')
#     # ChenHuan 2018/5/17 21:36 模型管理器 objects,使用 all() 方法从数据库里获取了全部的文章,存在了 articles 变量里.
#     # all方法返回的是一个QuerySet（可以理解成一个类似于列表的数据结构）.
#     # 由于通常来说博客文章列表是按文章发表时间倒序排列的,即最新的文章排在最前面,
#     # 所以我们紧接着调用了 order_by 方法对这个返回的 queryset 进行排序.
#     # 排序依据的字段是 created_time,即文章的创建时间.- 号表示逆序,如果不加 - 则是正序.
#     #  接着如之前所做,我们渲染了 blog\index.html 模板文件,并且把包含文章列表数据的 articles 变量传给了模板.
#     sentence = Ana.objects.get()
#     return render(request, 'blog/index.html',
#                   context={'articles': articles, 'sentence': sentence, })

class IndexView(ListView):
    """ ChenHuan 2017/4/7 16:30
    首页类视图,继承自ListView,用于展示从数据库中获取的文章列表
    """
    template_name = 'blog/index.html'
    # ChenHuan 2017/4/7 16:32 template_name属性用于指定使用那个模板进行渲染

    context_object_name = 'article_list'
    # ChenHuan 2017/4/7 16:34 context_object_name属性用于给上下文变量取名(在模板中使用该名字)

    def get_queryset(self):
        """ ChenHuan 2017/4/7 16:35
        复写 get_queryset 方法以增加获取 model 列表的其他逻辑,
        即过滤数据,获取所有已发布文章.
        """
        article_list = Article.objects.filter(status='p')
        # ChenHuan 2017/4/7 16:37 获取数据库中的所有已发布的文章,即filter(过滤)状态为'p'(已发布)的文章。

        return article_list

    def get_context_data(self, **kwargs):
        """ ChenHuan 2017/4/7 16:38
        复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问,
        即增加额外的数据,这里返回一个文章分类,以字典的形式
        """
        kwargs['sentence'] = Ana.objects.get()
        # ChenHuan 2018/5/18 15:55 获取语录

        return super(IndexView, self).get_context_data(**kwargs)
        # ChenHuan 2017/4/7 16:41 return super(IndexView, self).get_context_data(**kwargs) 语句的作用是添加了category_list 到上下文中,还要把默认的一些上下文变量也返回给视图函数,以便其后续处理。

class ArticleDetailView(DetailView):
    """ ChenHuan 2017/4/7 21:45
    Django有基于类的视图DetaileView,用于显示一个对象的详情页,则可以直接继承
    """
    model = Article
    # ChenHuan 2017/4/7 21:47 用于指定视图获取那个model

    template_name = "blog/detail.html"
    # ChenHuan 2017/4/7 21:48 用于指定用模板文件detail.html进行渲染

    context_object_name = "article"
    # ChenHuan 2017/4/7 21:51 用于指定在模板使用的上下文名字

    slug_url_kwarg = 'article_slug'
    # ChenHuan 2017/4/7 21:54 slug_url_kwarg用于接收一个来自url中的slug,然后会根据这个slug进行查询
    # ChenHuan 2017/4/7 21:56 在index.html中的模板标签定义了业务逻辑(即在url中指定参数),此处在urlpatterns捕获article_slug

    def get_object(self, queryset=None):
        """ ChenHuan 2017/4/7 22:02
        get_object() 返回该视图要显示的对象。
        如果有设置queryset,该queryset 将用于对象的源;
        否则,将使用get_queryset(). get_object()从视图的所有参数中查找slug_url_kwarg参数;
        如果找到了这个参数,该方法使用这个参数的值执行一个基于slug字段的查询.
        """
        obj = super(ArticleDetailView, self).get_object()

        # obj.body = markdown.markdown(obj.body,extensions = [
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        #     'markdown.extensions.toc',
        # ])
        # ChenHuan 2018/5/19 9:19 markdown 渲染函数传递了额外的参数 extensions,
        # 它是对 Markdown 语法的拓展,这里我们使用了三个拓展,分别是 extra、codehilite、toc.
        # extra 本身包含很多拓展,而 codehilite 是语法高亮拓展,这为我们后面的实现代码高亮功能提供基础,
        # 而 toc 则允许我们自动生成目录.
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks', 'toc'], )

        obj.toc = obj.body.toc_html

        return obj

    def get_context_data(self, **kwargs):
        """ ChenHuan 2017/4/8 19:10
        复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问,
        即增加额外的数据,这里返回一个文章分类,以字典的形式
        """
        kwargs['sentence'] = Ana.objects.get()
        # ChenHuan 2018/5/18 15:55 获取语录

        return super(ArticleDetailView, self).get_context_data(**kwargs)
        # ChenHuan 2017/4/8 19:16 return super(ArticleDetailView, self).get_context_data(**kwargs) 语句的作用是添加了article_category_list到上下文中,还要把默认的一些上下文变量也返回给视图函数,以便其后续处理。

class CategoryView(ListView):
    """ ChenHuan 2018/5/20 8:07
    分类视图,用于展示分类
    """
    model = Article

    template_name = 'blog/category.html'

    context_object_name = 'catedory_list'
    # queryset = Category.objects.annotate(article_num=Count('article'))

    def get_queryset(self):
        """ ChenHuan 2017/4/7 16:35
        复写 get_queryset 方法以增加获取 model 列表的其他逻辑.
        """
        catedory_list = Category.objects.all().order_by('name').annotate(article_num=Count('article'))
        # ChenHuan 2018/5/20 8:13 获取分类,.annotate(article_num=Count('article')) 统计分类文章

        return catedory_list

    def get_context_data(self, **kwargs):
        """ ChenHuan 2017/4/7 16:38
        复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问,
        即增加额外的数据,这里返回一个文章分类,以字典的形式
        """
        kwargs['sentence'] = Ana.objects.get()
        # ChenHuan 2018/5/18 15:55 获取语录

        return super(CategoryView, self).get_context_data(**kwargs)
        # ChenHuan 2017/4/7 16:41 return super(IndexView, self).get_context_data(**kwargs) 语句的作用是添加了category_list 到上下文中,还要把默认的一些上下文变量也返回给视图函数,以便其后续处理。

class CategoryArticleView(DetailView):
    """ ChenHuan 2017/4/8 17:11
    定义分类视图,用于展示该分类下的所有文章,同样继承自DetailView用于显示一个对象的详情页。
    """
    model = Category
    # ChenHuan 2017/4/8 18:05 用于指定视图获取那个model

    template_name = 'blog/categorys.html'
    # ChenHuan 2017/4/8 17:13 用于指定用模板文件category.html进行渲染

    context_object_name = 'categories_list'
    # ChenHuan 2017/4/8 17:15 指定模板中需要用到的上下文对象的名字

    slug_url_kwarg = 'category_slug'
    # ChenHuan 2017/4/8 17:52 slug_url_kwarg用于接收一个来自url中的slug,然后会根据这个slug进行查询

    def get_object(self, queryset=None):
        """ ChenHuan 2017/4/8 18:04
        get_object() 返回该视图要显示的对象。
        如果有设置queryset,该queryset 将用于对象的源;否则,将使用get_queryset(). get_object()从视图的所有参数中查找slug_url_kwarg参数;如果找到了这个参数,该方法使用这个参数的值执行一个基于slug字段的查询。
        """
        obj = super(CategoryArticleView, self).get_object()

        obj.declare = markdown2.markdown(obj.declare, extras=['fenced-code-blocks',], )

        return obj

    def get_context_data(self, **kwargs):
        """ ChenHuan 2017/4/8 18:16
        复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问,
        即增加额外的数据,这里返回一个文章分类信息,以字典的形式
        """
        context = super(CategoryArticleView, self).get_context_data(**kwargs)

        category = Category.objects.filter(slug=self.kwargs['category_slug'])
        # ChenHuan 2017/4/8 20:39 根据url中的category_slug参数去Category模型中筛选出文章分类信息

        context['article_list'] = Article.objects.filter(category=category, status='p')
        # ChenHuan 2017/4/8 19:31  获取数据库中Article中的所有该分类下的文章信息

        context['sentence'] = Ana.objects.get()
        # ChenHuan 2018/5/18 15:55 获取语录

        return context
        # ChenHuan 2017/4/8 18:19  return super(CategoryView, self).get_context_data(**kwargs) 语句的作用是添加了article_category_list到上下文中,还要把默认的一些上下文变量也返回给视图函数,以便其后续处理。

class ArchiveView(ListView):
    """ ChenHuan 2017/4/11 12:45
    归档视图,用于展示归档
    """
    template_name = "blog/archive.html"

    context_object_name = "article_list"

    def get_queryset(self):
        """ ChenHuan 2017/4/11 12:49
        复写 get_queryset 方法以增加获取 model 列表的其他逻辑.
        """
        # year = int(self.kwargs['year'])
        # month = int(self.kwargs['month'])
        article_list = Article.objects.filter(status='p')
        # created_time__year = year, created_time__month = month

        return article_list

    def get_context_data(self, **kwargs):
        """ ChenHuan 2017/4/8 18:16
        复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问,
        即增加额外的数据,这里返回一个文章分类信息,以字典的形式
        """
        kwargs['date_archive'] = Article.objects.archive()

        kwargs['sentence'] = Ana.objects.get()
        # ChenHuan 2018/5/18 15:55 获取语录

        return super(ArchiveView, self).get_context_data(**kwargs)
