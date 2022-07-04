from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView, DetailView


def index(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    directors = Director.objects.all()

    return render(request, 'movie_app/index.html', {
        'movies': movies,
        'actors': actors,
        'directors': directors,

    })


class ListMovie(ListView):
    template_name = 'movie_app/all_movies.html'
    context_object_name = 'movies'
    model = Movie


class DetailMovie(DetailView):
    template_name = 'movie_app/one_movie.html'
    context_object_name = 'movie'
    model = Movie


class ListDirector(ListView):
    template_name = 'movie_app/all_directors.html'
    context_object_name = 'directors'
    model = Director


class DetailDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'director'


class ListActor(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


class DetailActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'actor'
