from django.shortcuts import render, redirect
from officeshop.models.products import Product
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.http import HttpRequest
from django.contrib.auth.models import User
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



def register(request:HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            return redirect('home')
        return redirect('register')
    else:
        form = RegisterForm()
    return render (request, 'register.html', context={
        'title': 'Регистрация',
        'form':form,
    })

def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request,user)
                return redirect('home')
            
    else:
        form=LoginForm()
        return render(request, 'login.html', context={
            'title' : 'Авторизация',
            'form' : form,
        })
    return redirect('login')

def logout_user(request: HttpRequest):
    if request.method == 'POST':
        logout(request)

    return redirect('home')