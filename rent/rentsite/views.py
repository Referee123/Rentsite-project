from django.shortcuts import render

# Create your views here.
def  rentsites(request):
    return render(request, 'rentsite.html')