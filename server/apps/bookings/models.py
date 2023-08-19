from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booked_seats = models.PositiveIntegerField(default=1)
    booking_date = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    start_time = models.DateTimeField(db_index=True, default=timezone.now)
    available_seats = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.user} - Seats: {self.booked_seats}"
