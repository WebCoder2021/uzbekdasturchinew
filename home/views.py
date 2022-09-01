
from django.shortcuts import render
from blogPost.models import Post
# Create your views here.
def main(request):
    context = {}
    context['posts'] = Post.objects.all()
    return render(request,'home/main.html',context)