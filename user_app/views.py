from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse



# Create your views here.

def display(request):
    return render(request,'user_app/display.html')

def logout(request):
    request.session.flush()
    return redirect('user:login')

def login(request):
    if request.method=='POST':
        e=request.POST.get('email')
        p=request.POST.get('pass')
        user = UserModel.objects.filter(email=e,password=p)
        
        if(user.count()>0):
            for user in user:
                request.session['email']=user.email
                request.session['id']=user.id
                request.session['username'] = user.username
                return redirect('photo_app:index')

        else:
            return HttpResponse("wrong Crdentials")
    else:
        return render(request,'user_app/login.html')
     