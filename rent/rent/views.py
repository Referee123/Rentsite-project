from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def rentsite(request):
    return render(request, 'rentsite.html')    