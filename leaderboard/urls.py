from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAll, name='index'),
    path('leaderboard/upload/', views.updateBoard, name='upload'),
    path('leaderboard/<int:pk>/', views.details, name='leader_detail'),
]
