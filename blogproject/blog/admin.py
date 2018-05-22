#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:12
# @Author  : ChenHuan
# @Site    :
# @File    : models.py
# @Desc    : Django后台管理模块
# @Software: PyCharm

from django.contrib import admin
# ChenHuan 2018/5/18 11:13 导入Django后台管理admin模块
from blog.models import Article, Category, Ana
# ChenHuan 2018/5/18 11:13 导入blog应用定义的model,注册相应应用模块,即Django管理站点登记一个模型,
# 就会得到一个友好的用户界面:允许你生成对象列表;以及非常容易的编辑、创建、删除对象.

class ArticleAdmin(admin.ModelAdmin):
    """ ChenHuan 2018/5/18 11:23
    新建ArticleAdmin类,继承自admin.ModelAdmin,用于保存文章类的自定义配置,以供管理工具使用.
    """
    prepopulated_fields = {'slug': ('title',)}
    # ChenHuan 2018/5/18 11:24 prepopulated_fields属性用于告诉Django,slug是title的关联字段,即当输入文章标题时,slug字段会自动填充相应的内容。

    list_display = ('title', 'author', 'created_time', 'status', 'category',)
    # ChenHuan 2018/5/18 11:29 list_display属性允许你设置你想要在管理对象列表页面显示的模型字段.

class CategoryAdmin(admin.ModelAdmin):
    """ ChenHuan 2018/5/22 17:16
    用于保存文章分类的自定义配置
    """
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'declare')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ana)
# ChenHuan 2018/5/18 11:15 通过admin.site.register()注册相应app模块
