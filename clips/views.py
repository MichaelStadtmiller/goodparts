from django.shortcuts import render
from django.http import HttpResponse
from .getklips import *


# Create your views here.
# def index(request):
#     html = getURLS()
#     return HttpResponse(html)

def index(request):
    getURLS()
    return render(request, 'clips/index.html')
