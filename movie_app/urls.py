from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movie/<slug:slug>', views.DetailMovie.as_view(), name='movie-detail'),
    path('movie', views.ListMovie.as_view()),
    path('directors', views.ListDirector.as_view(), name='all_directors'),
    path('directors/<slug:slug>', views.DetailDirector.as_view(), name='director-detail'),
    path('actors', views.ListActor.as_view(), name='all_actors'),
    path('actors/<slug:slug>', views.DetailActor.as_view(), name='actor-detail'),
]
