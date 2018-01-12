#coding=utf8
from ..models import Post,Category
from django import template

register = template.Library()  # 暂时理解为标签仓库


# 通过注解将get_current_posts装饰为register.sinple_tag，这样就可以在模板中引用语法 {% get_recent_posts %}
@register.simple_tag
def get_current_posts(num=5):
    # 排序依据的字段是 created_time，即文章的创建时间。- 号表示逆序，如果不加 - 则是正序
    return Post.objects.all().order_by('-created_time')[:num]


# 按月份归档
@register.simple_tag
def archives():
    # dates返回一个列表，且为python的date元素，parameter 1：数据库字段，parameter 2：精准度，parameter 3：精准度
    return Post.objects.dates('created_time', 'month', 'DESC')

@register.simple_tag
def get_category():
    return Category.objects.all()


