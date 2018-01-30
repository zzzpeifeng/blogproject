# coding=utf-8
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView


# Create your views here.


class IndexView(ListView):
    model = Post  # 指定获取模型，Post
    template_name = 'blog/index.html'  # 指定视图渲染模板
    context_object_name = 'post_list'  # 指定获取模型列表数据保存变量名。


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})



# 归类返回--基于通用视图
# 与IndexView属性几乎一致，直接继承IndexView
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# 分类跳转
# def category(request, pk):
#     记得在开始部分导入 Category 类
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month).order_by("-created_time")


# 归档跳转
# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        response= super(PostDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response

    #获取对应的文章
    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form=CommentForm()
        comment_list=self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context


# 跳转详情
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    # extra
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    # 一对多查找，根据post对象找comment对象
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)
