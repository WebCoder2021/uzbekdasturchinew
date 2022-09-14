from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import CustomUser


# Create your views here.
def log_in(request):
    context = {}
    if request.method == "POST":
        post = request.POST
        phone = post.get('phone', False)
        password = post.get('password', False)
        user = post.get('user', False)
        if user:
            user1 = CustomUser.objects.filter(id=user).first()
            login(request,user1)
            return redirect('home')
        else:
            password2 = post.get('password2', False)
            if password == password2:
                first_name = post.get('first_name', False)
                last_name = post.get('last_name', False)
                middle_name = post.get('middle_name', False)
                email = post.get('email', False)
                location = post.get('location', False)
                if first_name and last_name and middle_name and location:
                    user = CustomUser.objects.create(
                        phone=phone, first_name=first_name, last_name=last_name, middle_name=middle_name)
                    if email:
                        user.email = email
                    if location:
                        user.location = location
                    user.set_password(password)
                    user.save()
                    print('user')
                    sign_in = authenticate(request, phone=phone, password=password)
                    if sign_in is not None:
                        login(request,user)
                        return redirect('home')
                    else: context['error'] = 'Login yoki parol xato'
                else: context['error'] = "Ma'lumotlar to'liq kiritilmadi"
            else:
                context['error'] = "Qayta kiritilgan parol xato"
                return render(request, 'users/login.html', context)
    return render(request, 'users/login.html',context)
def logout_view(request):
    context = {}
    msg =  request.GET.get('logout',False)
    if msg and msg == "true":
        logout(request)
        return redirect("home")
    return render(request, 'users/logout_view.html',context)

def check_user(request):
    phone=request.GET.get('phone')
    user = CustomUser.objects.filter(phone=phone).first()
    if user is not None:
        return JsonResponse({'user':user.id})
    return JsonResponse({'user':False})



def user_base(request):
    context = {}
    return render(request, 'users/user_base.html',context)
def profile(request):
    context = {}
    if request.method == 'POST':
        pic = request.FILES.get('picture',False)
        if pic:
            print
            request.user.picture = pic
            request.user.save()
    return render(request, 'users/profile.html',context)
def settings(request):
    context = {}
    if request.method == 'POST':
        post = request.POST
        first_name = post.get('first_name',False)
        last_name = post.get('last_name',False)
        middle_name = post.get('middle_name',False)
        email = post.get('email',False)
        location = post.get('location',False)
        pass1 = post.get('pass1',False)
        pass2 = post.get('pass2',False)
        pass3 = post.get('pass3',False)
        user = request.user
        if first_name and user.first_name != first_name:
            user.first_name = first_name
        if last_name and user.last_name != last_name:
            user.last_name = last_name
        if middle_name and user.middle_name != middle_name:
            user.middle_name = middle_name
        if email and user.email != email:
            user.email = email
        if location and user.location != location:
            user.location = location

        if pass1 and pass2 and pass3:
            if user.check_password(pass1):
                if pass2 == pass3:
                    user.set_password(pass2)
                else: context['err'] = "Qayta kiritilgan parol xato"
            else: context['err'] = "Joriy parol xato"

        user.save()
        login(request,user)
        context['msg'] = "Ma'lumotlar o'zgartirildi"
    return render(request, 'users/settings.html',context)
