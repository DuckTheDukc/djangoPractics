from django.contrib import admin
from officeshop.models import Product

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
