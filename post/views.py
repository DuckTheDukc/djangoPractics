from django.shortcuts import render
from django.http import HttpResponse

def get_hello(request):
    return render(request, 'base.html')

# Create your views here.
