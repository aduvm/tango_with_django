from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from markdown import markdown
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-create_time') #按时间倒序排列
    return render(request,'blog/index.html',context = {'post_list':post_list})
def detail(request,pk):
    post = Post.objects.get(id=pk)

    post.body = markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    post.excerpt = markdown(post.excerpt,
                         extensions=[
                             'markdown.extensions.extra',
                             'markdown.extensions.codehilite',
                             'markdown.extensions.toc',
                         ])
    return render(request,'blog/detail.html',context = {'post':post})

def full_width(request):
    return render(request,'blog/full-width.html')
def contact(request):
    return render(request,'blog/contact.html')
def about(request):
    return render(request,'blog/about.html')


