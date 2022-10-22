from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist, name='artist'),
    path('create/', views.createArtist, name='createArtist'),
]