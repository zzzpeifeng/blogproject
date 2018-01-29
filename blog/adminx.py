# _*_ coding:utf-8 _*_
import xadmin
from xadmin import views
from .models import Post, Category, Tag
from xadmin.views import BaseAdminPlugin,ListAdminView
from django.template import loader




class PostAdmin(object):
    list_display = ('title', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author')
    search_fields = ('title', 'created_time', 'modified_time', 'excerpt')
    list_filter = ('title', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author')
    list_export = ('csv', 'json')  # 导出选项
    # actions=[MyAction,]
    list_editable = ('category', 'tags')
    import_excel = True #导入
    data_charts = {
        "user_count": {'title': u"博客发布", "x-field": "created_time", "y-field": ("modified_time",),
                       "order": ('created_time',)
                       }
    }


class CategoryAdmin(object):
    list_display = ('name',)


class TagAdmin(object):
    list_display = ('name',)


class GlobalSetting(object):
    site_title = u'博客后台'
    site_footer = u'Copyright ZhangPeifeng'
    menu_style = 'accordion'


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
