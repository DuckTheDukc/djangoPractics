from django.urls import path
from .views import get_homepage, get_about, get_products, get_product_detail, search_product, register, login_user, logout_user, profile_view, cart_add, cart_detail, cart_remove, cart_remove_all, create_order 


urlpatterns = [
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
    path('', get_homepage, name='home'),
    path('product/<int:pk>', get_product_detail, name='product_detail'),
    path('search', search_product, name='search'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', profile_view, name='profile'),
    path('cart/add/<int:product_id>', cart_add , name='cart_add'),
    path('cart/remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('cart', cart_detail, name='cart_detail'),
    path('cart/remove/all', cart_remove_all, name='cart_remove_all'),
    path('order', create_order, name='create_order')
]