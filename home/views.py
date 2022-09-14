
from django.shortcuts import render
from blogPost.models import Post
from .models import FAQ, Email_send, SendMessages
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
    context['faqs'] = FAQ.objects.all()[:6]
    return render(request,'home/faq.html',context)

def contact(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email',False)
        message = request.POST.get('message',False)
        full_name = request.POST.get('name',False)
        if email and message and full_name:
            ms = SendMessages.objects.create(email=email, message=message, full_name=full_name)
            ms.save()
            context['ms'] = ms

    return render(request,'home/contact.html',context)

def bad_request(request,exception=None):
    return render(request,'404.html')
