from django.urls import path
from .views import get_book

urlpatterns = [
    path('', get_book)
]