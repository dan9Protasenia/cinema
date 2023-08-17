from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_posters/', default='default_poster.jpg')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
