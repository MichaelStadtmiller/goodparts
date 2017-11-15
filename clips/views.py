from django.shortcuts import render
from django.http import HttpResponse
from .getklips import *
import json


def scrape(request):
    for a in range(2000):
        getURLS()
    return HttpResponse(status=200)


def index(request):

    return render(request, 'clips/index.html')


def api_get_all_scenes(request):
    # get all scene data with movie data
    if request.method == 'GET':
        scene_array = []
        # MLS: filter for one movies only right now.
        all_scenes = Scene.objects.filter(movie__name='American Gangster')
        # all_scenes = Scene.objects.all()
        for s in all_scenes:
            scene_sub_array = {}
            # scene data
            scene_sub_array['scene_name'] = str(s.name)
            scene_sub_array['name_path'] = str(s.name_path)
            scene_sub_array['description'] = str(s.description)
            scene_sub_array['video_path'] = str(s.video_path)
            # movie data
            scene_sub_array['movie_name'] = str(s.movie.name)
            scene_sub_array['movie_name_path'] = str(s.movie.name_path)
            scene_sub_array['movie_description'] = str(s.movie.description)
            scene_sub_array['movie_poster'] = str(s.movie.poster)
            scene_sub_array['movie_date'] = str(s.movie.date_released)

            scene_array.append(scene_sub_array)
        return HttpResponse(json.dumps(scene_array))
    return HttpResponse(status=403)

# Given an actor n
def api_get_actor_scenes(request):
    # get all scene data with movie data
    if request.method == 'GET':
        actor_input = request.GET.get('actor')
        print(actor_input)

        all_actor_scenes = Scene.objects.filter(movie__role__actor__url='http://klipd.com/people/1769ngel-salazar')
        #all_actor_scenes = Scene.objects.filter(movie__role__actor__name_path=actor_input)
        scene_array = []

        # all_scenes = Scene.objects.all()
        for s in all_actor_scenes:
            scene_sub_array = {}
            # scene data
            scene_sub_array['scene_name'] = str(s.name)
            scene_sub_array['name_path'] = str(s.name_path)
            scene_sub_array['description'] = str(s.description)
            scene_sub_array['video_path'] = str(s.video_path)
            # movie data
            scene_sub_array['movie_name'] = str(s.movie.name)
            scene_sub_array['movie_name_path'] = str(s.movie.name_path)
            scene_sub_array['movie_description'] = str(s.movie.description)
            scene_sub_array['movie_poster'] = str(s.movie.poster)
            scene_sub_array['movie_date'] = str(s.movie.date_released)
            scene_sub_array['director'] = str(s.movie.director)

            scene_array.append(scene_sub_array)
        return HttpResponse(json.dumps(scene_array))
    return HttpResponse(status=403)


def test(request):
    a = request.GET.get('actor')
    return HttpResponse(a)
