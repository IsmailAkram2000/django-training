from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums.as_view()),
    path('create/', views.createAlbum.as_view(), name = 'Create Album'),
]