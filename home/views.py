
from django.shortcuts import render
from blogPost.models import Post
# Create your views here.
def posts(request):
    context = {}
    context['posts'] = Post.objects.all()
    return render(request,'post/posts.html',context)