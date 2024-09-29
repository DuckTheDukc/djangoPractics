from django.contrib import admin
from officeshop.models import Product
from officeshop.models.orderItem import OrderItem
from officeshop.models.order import Order

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer_user', 'customer_email', 'order_date', 'status')
    search_fields=('customer_user', 'customer_email', 'status')
    list_filter=('status', 'order_date')
    inlines=[OrderItemInline]