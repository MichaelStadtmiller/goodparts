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
