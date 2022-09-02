from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    context["categoryes"] = PostCategory.objects.all()
    context["popular_post"] = Post.objects.exclude(slug=slug).order_by('-postlike')[:3]
    context["tags"] = PostTags.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            cm = request.POST.get('message', False)
            if cm:
                com = Comment.objects.create(user=request.user,post=post,content=cm)
                com.save()
    context["comments"] = Comment.objects.filter(post=post).all()
    return render(request, 'post/blog_detail.html',context)


def like(request):
    return render(request, 'blog/blog_like.html')


def blog_like(request,slug):
    url = 'blog_detail'
    post = Post.objects.filter(slug=slug).first()
    if request.user.is_authenticated and post:
        like = PostLike.objects.get_or_create(post=post)[0]
        if request.user in like.users.all():
            like.users.remove(request.user)
        else:
           like.users.add(request.user)
           if PostDisLike.objects.filter(post=post).exists():
                  dislike = PostDisLike.objects.filter(post=post)[0]
                  dislike.users.remove(request.user)
                  dislike.save()
        like.save()
    if url == "blog_detail":
       return HttpResponseRedirect(reverse(url, args=[slug]))
    else: return HttpResponseRedirect(reverse(url))

def blog_dislike(request,slug):
    url = 'blog_detail'
    post = Post.objects.filter(slug=slug)[0]
    if request.user.is_authenticated and post:
        dislike = PostDisLike.objects.get_or_create(post=post)[0]
        if request.user in dislike.users.all():
            dislike.users.remove(request.user)
        else:
            dislike.users.add(request.user)
            if PostLike.objects.filter(post=post).exists():
                   like = PostLike.objects.filter(post=post)[0]
                   like.users.remove(request.user)
                   like.save()
        dislike.save()
    if url == "blog_detail":
       return HttpResponseRedirect(reverse(url, args=[slug]))
    else: return HttpResponseRedirect(reverse(url))