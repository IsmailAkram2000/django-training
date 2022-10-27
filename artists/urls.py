from django.urls import path
from . import views

urlpatterns = [
    path('', views.allArtists.as_view(), name='Get All Artists'),
    path('create/', views.createArtist.as_view(), name='Create Artist'),
]