
from django.shortcuts import render
from blogPost.models import Post
from .models import FAQ
# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all()[:6]
    return render(request,'home/home.html',context)
def faq(request):
    context = {}
    context['FAQs'] = FAQ.objects.all()[:6]
    return render(request,'home/faq.html',context)