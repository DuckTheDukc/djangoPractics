from django.db import models

class book(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=10)
    year=models.DateField(null=True)

class Author(models.Model):
    name=models.CharField(max_length=255)
    date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=255)
# Create your models here.
