from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=100)
    birth_date=models.DateField(null=True)

class publisher(models.Model):
    name= models.CharField(max_length=100)
    established=models.DateField(null=True)
    
class book(models.Model):
    title=models.CharField(max_length=100)
    publications_date=models.DateField(null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers=models.ManyToManyField(publisher)
# Create your models here.
