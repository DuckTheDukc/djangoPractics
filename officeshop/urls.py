from django.urls import path
from .views import get_homepage, get_about, get_products, get_product_detail, search_product, register, login_user, logout_user


urlpatterns = [
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
    path('', get_homepage, name='home'),
    path('product/<int:pk>', get_product_detail, name='product_detail'),
    path('search', search_product, name='search'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout')
]