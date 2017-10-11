from django.shortcuts import render
from django.http import HttpResponse
from .getklips import *


def scrape(request):
    for a in range(200):
        getURLS()
    return HttpResponse(status=200)


def index(request):
    return render(request, 'clips/index.html')
