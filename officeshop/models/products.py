from django.db import models
 
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image=models.ImageField(upload_to="products/%Y/%m/%d", null=True)
    
    
    