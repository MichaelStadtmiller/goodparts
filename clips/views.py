from django.shortcuts import render
from django.http import HttpResponse
from .getklips import *


def index(request):
    for a in range(200):
        getURLS()
    return render(request, 'clips/index.html')
