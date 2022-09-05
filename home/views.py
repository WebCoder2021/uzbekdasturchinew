
from django.shortcuts import render
from blogPost.models import Post
from .models import FAQ, Email_send
# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all()[:6]
    if request.method == 'POST':
        email = request.POST.get('email',False)
        if request.user.is_authenticated and email:
            mail = Email_send.objects.create(email=email,user=request.user)
            mail.save()
        if email and not request.user.is_authenticated:
            mail = Email_send.objects.create(email=email)
            mail.save()
    return render(request,'home/home.html',context)

def faq(request):
    context = {}
    context['FAQs'] = FAQ.objects.all()[:6]
    return render(request,'home/faq.html',context)

def contact(request):
    context = {}
    return render(request,'home/contact.html',context)