from django.conf.urls import url
from clips.views import *


urlpatterns = [
    url(r'^$', index.as_view(), name='index'),
    url(r'^scrape/', scrape.as_view(), name='scrape'),
    url(r'^api/get_all_scenes/$', api_get_all_scenes.as_view(), name='get all scenes'),
    url(r'^api/get_some_scenes/$', api_get_some_scenes.as_view(), name='get some scenes'),
    url(r'^api/get_actor_scenes/$', api_get_actor_scenes.as_view(), name='get actor scenes'),
    url(r'^api/get_decade_scenes/$', api_get_decade_scenes.as_view(), name='get decade scenes'),
    url(r'^api/get_movie_scenes/$', api_get_movie_scenes.as_view(), name='get movie scenes'),
]
