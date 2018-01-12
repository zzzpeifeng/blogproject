#coding=utf8
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment                                   #标明表单对应一个Comment数据库模型
        fields=['name','email','url','text']        #指定了表单需要显示的字段