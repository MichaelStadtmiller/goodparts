from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scrape/', views.scrape, name='scrape'),
    url(r'^api/get_all_scenes/$', views.api_get_all_scenes, name='get all scenes'),
    url(r'^api/get_some_scenes/$', views.api_get_some_scenes, name='get some scenes'),
    url(r'^api/get_actor_scenes/$', views.api_get_actor_scenes, name='get actor scenes'),
    url(r'^api/get_decade_scenes/$', views.api_get_decade_scenes, name='get decade scenes'),
    url(r'^api/get_movie_scenes/$', views.api_get_movie_scenes, name='get movie scenes'),
]
