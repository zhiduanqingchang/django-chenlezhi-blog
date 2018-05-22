from django.apps import AppConfig
# from suit.apps import DjangoSuitConfig
# ChenHuan 2018/5/21 18:48 admin后台采用suit美化

class BlogConfig(AppConfig):
    name = 'blog'

# class SuitConfig(DjangoSuitConfig):
#     layout = 'horizontal'
    # ChenHuan 2018/5/21 18:49 layout这个参数决定你的网页是初始样式是垂直样式还是水平样式,可选参数为‘horizontal’或‘vertical’.