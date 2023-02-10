from django.shortcuts import render
from .models import ProductsDescriptionHiFi, ProductsDescriptionVinyl

# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def productdescription(request):
    allvinyl = ProductsDescriptionVinyl.objects.all()  # select * from cars;

    context = {
        'allvinyl': allvinyl

    }

    return render(request, 'products/productdescription.html', context)


# def allvinyl(request):
#     allvinyl = ProductsDescriptionVinyl.objects.all() #select * from cars;
#
#     context