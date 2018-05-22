#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/10 21:42
# @Author  : ChenHuan
# @Site    :
# @File    : custom_markdown.py
# @Desc    : 自定义markdown模板标签
# @Software: PyCharm

import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    """ ChenHuan 2018/5/22 17:13
    实现在Django中解析markdown文本
    """
    return mark_safe(markdown2.markdown(force_text(value),
            extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables","spoiler"]))