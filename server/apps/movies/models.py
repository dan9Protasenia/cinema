from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_posters/', default='movie_posters/default_poster.jpg')
    genres = models.CharField()
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    production = models.CharField()
    time = models.CharField()

    def __str__(self):
        return self.title
