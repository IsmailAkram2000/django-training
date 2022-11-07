from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.userDetail.as_view(), name='user details'),
]