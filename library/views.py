from django.shortcuts import render

# Create your views here.
def get_book(request):
    return render(request, 'book.html', {'title': '451 градус по фаренгейту', 'content': 'Страница книги "451 градус по фаренгейту"'})