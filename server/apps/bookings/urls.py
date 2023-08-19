from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('schedule/', views.schedule, name='schedule'),
]
