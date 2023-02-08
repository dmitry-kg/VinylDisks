from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def productdescription(request):
    return render(request, 'products/productdescription.html')