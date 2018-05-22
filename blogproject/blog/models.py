#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 15:51
# @Author  : ChenHuan
# @Site    :
# @File    : models.py
# @Desc    : 文件主要用一个Python类来描述数据表.称为模型(model).运用这个类,你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录而无需写一条又一条的SQL语句.
# @Software: PyCharm

from django.db import models
# ChenHuan 2018/5/17 15:57 和 model 相关的一些API定义在 django.db.models 模块中
from django.contrib.auth.models import User
# ChenHuan 2018/5/17 16:47  引入Django本身自带的User模块(主要用于用户验证)
from uuslug import uuslug
# ChenHuan 2017/4/7 10:15 pip install django-uuslug 引入安装的uuslug模块.
# django-uuslug是一个很方便的将中文转化成拼音slug的插件,通过使用django-uuslug,可以保确保slug是唯一的,并且都是unicode编码的.
from django.core.urlresolvers import reverse
# from simditor.fields import RichTextField
from collections import defaultdict

class ArticleManage(models.Manager):
    """ ChenHuan 2017/4/11 11:03
    自定义Manage(管理器),继承自默认的Manage,为其添加一个自定义的archive方法
    """
    def archive(self):
        """ ChenHuan 2017/4/11 11:05

        """
        date_list = Article.objects.datetimes('created_time', 'month', order='DESC')
        # ChenHuan 2017/4/11 11:07 获取到降序排列的精确到月份且已去重的文章发表时间列表,并把列表转为一个字典,字典的键为年份,值为该年份下对应的月份列表

        date_dict = defaultdict(list)

        for d in date_list:
            date_dict[d.year].append(d.month)
            # ChenHuan 2017/4/11 11:08 模板不支持defaultdict,因此我们把它转换成一个二级列表,由于字典转换后无序,因此重新降序排序

        return sorted(date_dict.items(), reverse=True)


class Category(models.Model):
    """ ChenHuan 2018/5/17 16:36
    Django 要求模型必须继承 models.Model 类.
    类Category对应着数据库Category表,用于存储文章的分类信息.
    Category 只需要一个简单的分类名 name 就可以了,
    CharField 指定了分类名 name 的数据类型,CharField 是字符型,
    CharField 的 max_length 参数指定其最大长度,超过这个长度的分类名就不能被存入数据库,
    当然 Django 还为我们提供了多种其它的数据类型,如日期时间类型 DateTimeField、整数类型 IntegerField 等等.
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField('类名', max_length=100)
    # ChenHuan 2018/5/17 16:36 文章分类的类名

    declare = models.TextField('分类描述', max_length=300, blank=True, null=True)
    # ChenHuan 2017/4/7 13:13 文章分类的说明

    slug = models.SlugField('slug', blank=True)

    # ChenHuan 2017/4/7 11:02 slug用于生成一个有意义（valid, meaninful）URL

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # ChenHuan 2017/4/7 11:03
        # if not self.slug:
        self.slug = uuslug(self.name, instance=self, start_no=9, max_length=200, word_boundary=True)
        super(Category, self).save(*args, **kwargs)
        # ChenHuan 2017/4/7 11:03 对文章分类在链接时能更好的读懂url,则需要使用uuslug

    def get_absolute_url(self):
        """ ChenHuan 2017/4/11 13:50
        reverse 解析 blog:detail 视图函数对应的 url
        """
        return reverse('blog:category', kwargs={'category_slug': self.slug})

# class Tag(models.Model):
#     """ ChenHuan 2018/5/17 16:37
#     类Tag对应着数据库Tag表,用于存储文章标签信息
#     """
#     name = models.CharField('标签名', max_length=100)
#
#     # ChenHuan 2018/5/17 16:37 文章标签的标签名
#
#     def __str__(self):
#         return self.name


class Article(models.Model):
    """ ChenHuan 2018/5/17 16:40
    定义Article模型,其包含文章标题、作者、发布时间、修改时间、正文、分类、标签.
    类Aticle 即表示Blog 的文章,一个类被 diango 映射成数据库中对应的一个表,表名即类名,
    类的属性(field),比如下面的title、content 等对应着数据库表的属性列.
    """
    STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'),)

    objects = ArticleManage()
    # ChenHuan 2017/4/11 12:06 调用自定义的Manage

    title = models.CharField('文章标题', max_length=100)
    # ChenHuan 2018/5/17 16:44 文章标题,CharFiled是用于存储字符串,即表示数据库中对应字段(列)用来存储字符串,'文章标题'作为位置参数(verbose_name)(字段说明),主要用于Django的后台系统,max_length表示能存储的字符串的最大长度.
    body = models.TextField('正文')
    # ChenHuan 2018/5/19 23:52 文章正文,TextField用以存储大文本字符(长文本).
    # body = RichTextField('正文')
    # ChenHuan 2018/5/17 16:49 文章正文,RichTextField django-simditor 一个 django 的富文本编辑器.
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # ChenHuan 2018/5/17 16:50  文章创建时间,DateTimeField用于存储时间,
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # ChenHuan 2018/5/17 16:50  文章最后一次修改时间,auto_now=True表示每次修改文章时自动添加修改的时间.
    # excerpt = models.CharField(max_length=300, blank=True)
    # ChenHuan 2018/5/17 16:54 文章摘要,可以没有文章摘要,但默认情况下 CharField 要求我们必须存入数据,否则就会报错.
    category = models.ForeignKey(Category)
    # tags = models.ManyToManyField(Tag, blank=True)
    # ChenHuan 2018/5/17 16:56  这是分类与标签,分类与标签的模型我们已经定义在上面.
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来,但是关联形式稍微有点不同.
    # 我们规定一篇文章只能对应一个分类,但是一个分类下可以有多篇文章,所以我们使用的是 ForeignKey,即一对多的关联关系.
    # 而对于标签来说,一篇文章可以有多个标签,同一个标签下也可能有多篇文章,所以我们使用 ManyToManyField,表明这是多对多的关联关系.
    # 同时我们规定文章可以没有标签,因此为标签 tags 指定了 blank=True.
    # ForeignKey、ManyToManyField 更多信息可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    author = models.ForeignKey(User)
    # ChenHuan 2018/5/17 17:00  文章作者,这里 User 是从 django.contrib.auth.models 导入的.
    # django.contrib.auth 是 Django 内置的应用,专门用于处理网站用户的注册、登录等流程,User 是 Django 为我们已经写好的用户模型.
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来.
    # 因为我们规定一篇文章只能有一个作者,而一个作者可能会写多篇文章,因此这是一对多的关联关系,和 Category 类似.
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    # ChenHuan 2018/5/18 11:26 显示文章状态的属性,使用一个选择参数,所以status的值只能被设置为一个给定的选择
    # STATUS_CHOICES,field 的 choices 参数需要的值,choices选项会使该field在被渲染成form时被渲染为一个select组件,
    # 这里我定义了两个状态,一个是Draft(草稿),一个是Published(已发布),select组件会有两个选项：Draft 和 Published.
    # 但是存储在数据库中的值分别是'd'和'p'，这就是 choices的作用.

    slug = models.SlugField('slug', blank=True)
    # ChenHuan 2018/5/18 15:36  slug是一个新闻属性,django中的slug是指有效URL的一部分,能使URL更加清晰易懂.

    def __str__(self):
        # ChenHuan 2017/4/7 9:35 主要用于交互解释器显示表示该类的字符串
        return self.title
        # ChenHuan 2017/4/7 9:36 Django使用__str__()方法,用文章的标题来代替名称'object'.如果不定义__str__()方法,模型生成的实例对象将会以’object‘这个名字显示在django的管理站点,不宜于管理和修改.

    class Meta:
        # ChenHuan 2017/4/7 9:38 模型类中的元类（Meta）包含元数据,ordering属性定义了文章的排序顺序.
        ordering = ['-created_time']
        # ChenHuan 2017/4/7 9:39 Meta 包含一系列选项,这里的 ordering 表示排序,- 号表示逆序.即当从数据库中取出文章时,其是按文章最后一次修改时间逆序排列的.

    def save(self, *args, **kwargs):
        # ChenHuan 2017/4/7 11:00
        # if not self.slug:
        self.slug = uuslug(self.title, instance=self, start_no=1, max_length=200, word_boundary=True)
        super(Article, self).save(*args, **kwargs)
        # ChenHuan 2017/4/7 11:00 重写save方法,将文章标题由任意编码转为相应的unicode(中文对应着拼音),start_no用于指定起始数字(即遇到值相同时会在末尾增加数字)

    def get_absolute_url(self):
        """ ChenHuan 2017/4/11 13:50
        reverse 解析 blog:detail 视图函数对应的 url
        """
        return reverse('blog:detail', kwargs={'article_slug': self.slug})


class Ana(models.Model):
    """ ChenHuan 2018/5/18 10:35
    类Ana对应着数据库Ana表,用于存储语录
    """
    sentence = models.TextField('语录')
    # ChenHuan 2018/5/18 10:41 美好的句子或一段话

    def __str__(self):
        return self.sentence