from django.shortcuts import render
from officeshop.models.products import Product
# Create your views here.

def get_homepage(request): 
    return render(request, 'home.html')

def get_about(request): 
    return render(request, 'about.html')

def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products.html', context ={"products": products,})
