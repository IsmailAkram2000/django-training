from django.urls import path
from . import views

urlpatterns = [
    path('', views.allAlbums.as_view()),
    path('filter/', views.AlbumListManual.as_view()),
]