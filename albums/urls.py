from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums, name = 'album'),
    path('create/', views.createAlbum, name = 'createAlbum'),
]