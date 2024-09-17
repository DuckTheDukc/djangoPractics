from django.urls import path
from .views import get_homepage, get_about, get_products

urlpatterns = [
    path('home/', get_homepage),
    path('about/', get_about),
    path('products/', get_products),
]