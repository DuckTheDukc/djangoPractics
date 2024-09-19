from django.shortcuts import render, redirect
from officeshop.models.products import Product
from django.db.models import Q
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

def search_product(request):
    if request.method=="GET":
        search=request.GET['search']
        products=Product.objects.filter(
            Q(name__icontains = search) | Q(description__icontains = search))
        return render (request, template_name='products.html', context={
        'products':products,
        'name':'канцтовары'
    })
    return redirect ('home')