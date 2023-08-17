from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from server.apps.movies.models import Movie


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booked_seats = models.PositiveIntegerField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seats: {self.booked_seats}"
