from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import MovieForm
from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_list')
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})
