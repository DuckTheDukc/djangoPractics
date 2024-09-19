from django.urls import path
from .views import get_homepage, get_about, get_products, get_product_detail, search_product


urlpatterns = [
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
    path('', get_homepage, name='home'),
    path('product/<int:pk>', get_product_detail, name='product_detail'),
    path('search', search_product, name='search')
]