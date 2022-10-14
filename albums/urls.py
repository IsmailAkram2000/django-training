from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums, name='artist'),
]