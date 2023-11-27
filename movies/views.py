from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies' : movies})

def details(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'movies/details.html', { 'movie' : movie })
    except:
        return render(request, 'movies/error404.html')