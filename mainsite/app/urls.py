from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard , name="dashboard"),
    path('delete/', views.delete_consume, name="delete"),
]