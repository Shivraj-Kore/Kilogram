from django.shortcuts import render

def homeScreen(request):
    context={}
    return render(request ,  "home.html" , context)

def registerView(request):
    return render(request ,  "register.html")