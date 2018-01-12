#coding=utf8
from __future__ import unicode_literals
from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100) #姓名
    email = models.EmailField(max_length=255) #邮箱
    url = models.URLField(blank=True)   #个人网站
    text = models.TextField()   #评论内容
    created_time = models.DateTimeField(auto_now_add=True)  #创建时间

    post = models.ForeignKey('blog.Post')  #一篇文章可以有多个评论，一对多关系

    def __str__(self):
        return self.text[:20]
