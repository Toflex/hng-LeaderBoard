from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leaderboard/', views.index, name='leaderboard'),
]
