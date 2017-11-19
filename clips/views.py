from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .getklips import *
import json


def scrape(request):
    for a in range(2000):
        getURLS()
    return HttpResponse(status=200)


def index(request):
    movie_count = Movie.objects.count()
    actor_count = Actor.objects.count()
    scene_count = Scene.objects.count()
    return render(request, 'clips/index.html', {'movie_count': movie_count,
                                                'actor_count': actor_count,
                                                'scene_count': scene_count})


###
# Return a json list of all movie scenes
###
def api_get_all_scenes(request):
    if request.method == 'GET':
        # MLS: filter for one movies only right now.
        #all_scenes = Scene.objects.filter(movie__name='American Gangster')
        all_scenes = Scene.objects.all()

        return HttpResponse(get_scene_data(all_scenes))
    return HttpResponse(status=403)


###
# Given an actor id from request
# Return a json list of scenes for that actor
###
def api_get_actor_scenes(request):
    if request.method == 'GET':
        actor_input = request.GET.get('actor')
        all_actor_scenes = Scene.objects.filter(movie__role__actor__id=actor_input)
        return HttpResponse(get_scene_data(all_actor_scenes), content_type="application/json")
    return HttpResponse(status=403)


###
# Given a decade in request
# Return a json list of scenes for that year
###
def api_get_decade_scenes(request):
    if request.method == 'GET':
        decade_input = request.GET.get('decade')[:3]
        all_decade_scenes = Scene.objects.filter(movie__date_released__startswith=decade_input)

        return HttpResponse(get_scene_data(all_decade_scenes), content_type="application/json")
    return HttpResponse(status=403)


###
# Given a movie id from request
# Return a json list of scenes for that movie
###
def api_get_movie_scenes(request):
    if request.method == 'GET':
        movie_input = request.GET.get('movie')
        all_movie_scenes = Scene.objects.filter(movie__id=movie_input)
        return HttpResponse(get_scene_data(all_movie_scenes), content_type="application/json")
    return HttpResponse(status=403)


###
# Given a Django QuerySet of scenes
# Return json list of scene data
###
def get_scene_data(scenes_query_set):
    scene_array = []

    # all_scenes = Scene.objects.all()
    for s in scenes_query_set:
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
    return json.dumps(scene_array)
