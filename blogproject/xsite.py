# -*- coding:utf-8 -*-
from xadmin import Settings
from xadmin.views.list import ListAdminView
from xadmin.views import CommAdminView
from xadmin.plugins.actions import BaseActionView,ActionPlugin
from django.http import HttpResponse, HttpResponseRedirect
from xadmin import views
import xadmin



class Base(Settings):
    enable_themes = True
    use_bootswatch = True
    # menu_style = 'default'
# class List(ListAdminView):
    # ListAdminView.list_per_page = 20


