
from django.http import HttpResponse


def get_hello(request):
    return HttpResponse('<h1>Привет!<h1>')
# Create your views here.
