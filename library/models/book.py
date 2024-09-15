from django.db import models
from .publisher import Publisher
from .author import Author


class Book(models.Model):
    title=models.CharField(max_length=100)
    publications_date=models.DateField(null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers=models.ManyToManyField(Publisher)