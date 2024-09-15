from django.shortcuts import render
from .models import Book

def get_info(request):
    book= Book.objects.get(id=1)
    return render(request, 'base.html', context={
        'book': book,
    })
# def get_author(request):
#     book_author=Book.objects.filter(author__name="Александр Сергеевич Пушкин")
#     return render(request, 'author.html', context={
#     'book_author': book_author,
#     })
def get_author(request):
    book_author=Book.objects.filter(author__name="Говард Филлипс Лавкрафт")
    return render(request, 'author.html', context={
    'book_author': book_author,
    })
def get_publisher(request):
    book_publisher=Book.objects.filter(publishers__name="hobby worlds")
    return render(request, 'publisher.html', context={
    'book_publisher': book_publisher,
    })
# Create your views here.
