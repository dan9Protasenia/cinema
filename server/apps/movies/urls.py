from django.conf.urls.static import static
from django.urls import path

from server import settings
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('create_movie/', views.create_movie, name='create_movie'),
    path('<int:pk>/delete/', views.delete_movie, name='delete_movie'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
