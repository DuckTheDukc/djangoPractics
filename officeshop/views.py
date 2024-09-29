from django.shortcuts import render, redirect, get_object_or_404
from officeshop.models.products import Product
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, OrderForm
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .cart import CartSession
from officeshop.models.products import Product
from django.urls import reverse
from officeshop.models.profile import Profile
from officeshop.models.orderItem import OrderItem
from officeshop.models.order import Order
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

@login_required(login_url='login')
def profile_view(request:HttpRequest):
    user=Profile.objects.select_related('user').get(user=request.user)
    if request.method == 'POST':
        user.gender = request.POST['gender']
        user.country = request.POST['country']
        user.city = request.POST['city']
        user.street = request.POST['street']
        user.house = request.POST['house']
        user.apartament_number = request.POST['apartment_number']
        
        user.save()
    return render(request, 'profile.html', context={
        'user': user
    })
    
    
    
    
    
def cart_add(request: HttpRequest, product_id):
    cart=CartSession(request.session)
    product=get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    
    return redirect(reverse('cart_detail'))

def cart_remove(request:HttpRequest, product_id):
    cart=CartSession(request.session)
    product=get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect(reverse('cart_detail'))

def cart_detail(request:HttpRequest):
    cart=CartSession(request.session)
    return render(request,'cart_detail.html', context={
        'cart':cart
    })

def cart_remove_all(request:HttpRequest):
    cart=CartSession(request.session)
    cart.clear()
    return redirect('cart_detail')




@login_required(login_url='login')
def create_order(request:HttpRequest):
    cart = CartSession(request.session)
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(customer_user=request.user, customer_email=form.data.get('customer_email'), )
            for item_cart in cart:
                print(item_cart)
                OrderItem.objects.create(order=order, product=item_cart['product'], quantity=item_cart['quantity']).save()
            cart.clear()
            return redirect('profile')
        form= OrderForm()
    else:
      form= OrderForm()
      return render(request, 'order.html',{
          'form':form
      })