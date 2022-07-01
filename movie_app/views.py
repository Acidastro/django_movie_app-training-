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


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('name').asc(nulls_last=True))
    movies = Movie.objects.annotate(
        false_bool=Value(True),
        true_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(533),
        new_budget=F('budget') + 100,
        year_plus_rating=F('rating') + F('year'),

    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })


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
