#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 10:43
# @Author  : ChenHuan
# @Site    : 
# @File    : article_filter.py
# @Desc    : 自定义FILTER模板标签
# @Software: PyCharm

from django import template

register = template.Library()

# @register.filter(is_safe=True)
@register.assignment_tag
def article_filter(q, **kwargs):
    """ ChenHuan 2018/5/21 10:48
    实现在template中执行数据库过滤查询
    """
    return q.filter(**kwargs)