from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def posts(request):
    context = {}
    posts = Post.objects.all()
    paginator = Paginator(posts.order_by('-create_date'), 6)
    page_number = request.GET.get('page')
    context["posts"] = paginator.get_page(page_number)
    return render(request, 'post/blog.html',context)

def blog_detail(request,slug):
    context = {}
    post = Post.objects.filter(slug=slug).first()
    context["post"] = post
    context["comments"] = Comment.objects.filter(post=post).all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('###### You are  authenticated')
            cm = request.POST.get('message', False)
            if cm:
                com = Comment.objects.create(user=request.user,post=post,content=cm)
                com.save()
                return render(request, 'post/blog_detail.html',context)

    return render(request, 'post/blog_detail.html',context)