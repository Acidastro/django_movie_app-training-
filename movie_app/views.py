from django.shortcuts import render, get_object_or_404
from .models import Movie, Director
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movie(request):
    # метод all достает все данные из объекта
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


def show_one_movie(request, slug_movie: str):
    # метод get достает данные об одном объекте
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_all_directors(request):
    directors = Director.objects.all()

    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
    })


def show_one_director(request, slug_director: str):
    # метод get достает данные об одном объекте
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director,
    })
