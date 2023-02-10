from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def aboutus(request):
    return render(request, 'website/aboutus.html')

def contactus(request):
    return render(request, 'website/contactus.html')

