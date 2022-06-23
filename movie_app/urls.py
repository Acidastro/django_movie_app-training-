from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.show_all_directors, name='all_directors'),
    path('directors/<slug:slug_director>', views.show_one_director, name='directors-detail'),
]
