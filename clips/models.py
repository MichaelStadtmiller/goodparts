from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    name_path = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True)
    poster = models.CharField(max_length=500, null=True)
    studio = models.CharField(max_length=100, null=True)
    genres = models.TextField(null=True)
    year_released = models.IntegerField(null=True)


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)
    role = models.CharField(max_length=100, null=True)


class Scene(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_path = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True)
    video_path = models.CharField(max_length=500)


decades = [
    '2016',
    # '2015',
    # '2014',
    # '2013',
    # '2012',
    # '2011',
    # '2010',
    # '2000s',
    # '1990s',
    # '1980s',
    # '1970s',
    # '1960s',
    # '1950s',
    # '1940s',
    # '1930s'
]

alphabet = [
    '0',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]