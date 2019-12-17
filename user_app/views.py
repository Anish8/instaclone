from django.shortcuts import render


# Create your views here.

def display(render):
    return render(request,'user_app/display.html')