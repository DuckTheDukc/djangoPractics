from django.db import models
from officeshop.models.order import Order
from officeshop.models.products import Product

class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    def __str__(self):
        return f'{self.quantity} of {self.product} for {self.order}'