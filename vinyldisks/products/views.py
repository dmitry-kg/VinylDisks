from django.shortcuts import render
from .models import ProductsDescriptionHiFi, ProductsDescriptionVinyl
from django.core.paginator import Paginator

# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def productdescription(request):
    new_vinyls = ProductsDescriptionVinyl.objects.order_by('-create_date')
    allvinyl = ProductsDescriptionVinyl.objects.all()  # select * from cars;
    paginator = Paginator(new_vinyls,6)
    page = request.GET.get('page')
    paged_vinyls = paginator.get_page(page)


    context = {
        'allvinyl': allvinyl,
        'new_vinyls': new_vinyls,
        'paged_vinyls': paged_vinyls,
    }

    return render(request, 'products/productdescription.html', context)


def productdescriptionhifi(request):
    allhifi = ProductsDescriptionHiFi.objects.all()  # select * from cars;

    context = {
        'allhifi': allhifi

    }

    return render(request, 'products/productdescription.html', context)
