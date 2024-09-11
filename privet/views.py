from django.http import HttpResponse
from django.shortcuts import render

def get_hello(request):
    # return HttpResponse('<h1>Привет!<h1>')
    return render(request, 'hello.html', {'title': 'Hello'})
# Create your views here.
