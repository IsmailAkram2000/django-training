from django.urls import path
from . import views

urlpatterns = [
    path('login_page/', views.Login.as_view(), name='Login'),
]