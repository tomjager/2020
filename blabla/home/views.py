from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def other(request):
    return render(request, 'others.html')
