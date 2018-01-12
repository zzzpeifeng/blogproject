#coding=utf-8
from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #正则表达式：捕获 [0-9]+到名为pk的组里
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #year为4位数，month位1~2位数
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #正则表达式：捕获[0-9]+到名为pk的组中
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]