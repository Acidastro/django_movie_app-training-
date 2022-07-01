from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('movie', views.show_all_movie),
    path('directors', views.ListDirector.as_view(), name='all_directors'),
    path('directors/<slug:slug_director>', views.show_one_director, name='directors-detail'),
    path('actors', views.ListActor.as_view(), name='all_actors'),
    path('actors/<slug:slug_actors>', views.show_one_actor, name='actors-detail'),
]
