from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scrape/', views.scrape, name='scrape'),
    url(r'^api/get_all_scene', views.api_get_all_scenes, name='get all scenes'),
]
