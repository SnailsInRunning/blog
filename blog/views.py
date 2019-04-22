from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.



#创建视图函数
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts':posts})
def post_detail(request,year,month,day,post):
#     post = get_object_or_404(post,slug=post,
#                                   status = 'published',
#                                   publish__year = year,
#                                   publish__month = month,
#                                   publish__day = day
#                             )

    post = Post.published.filter(slug=post)[0]
    return render(request,'blog/post/detail.html',{'post': post})