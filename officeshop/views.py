from django.shortcuts import render
from officeshop.models.products import Product
# Create your views here.

def get_homepage(request): 
    return render(request, 'home.html')

def get_about(request): 
    return render(request, 'about.html')

def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context ={"products": products,})

def get_product_detail(request, pk):
    product=Product.objects.get(pk=pk)
    return render(request, 'detail_product.html', context={'product':product})