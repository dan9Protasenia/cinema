from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Movie, Booking


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        booked_seats = int(request.POST.get('booked_seats', 1))
        booking = Booking.objects.create(user=request.user, movie=movie, booked_seats=booked_seats)
        return HttpResponseRedirect(request.path_info)

    return render(request, 'movies/movie_detail.html', {'movie': movie})


def schedule(request):
    bookings = Booking.objects.all()
    return render(request, 'movies/schedule.html', {'bookings': bookings})
