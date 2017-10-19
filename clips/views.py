from django.shortcuts import render
from django.http import HttpResponse
from .getklips import *


def scrape(request):
    for a in range(200):
        getURLS()
    return HttpResponse(status=200)


def index(request):
    return render(request, 'clips/index.html')


def api_get_all_scenes(request):
    if request.method == 'GET':
        movie_array = []
        #all_clips =

        #return HttpResponse(json.dumps(movie_array))
        return HttpResponse(status=200)
    return HttpResponse(status=403)