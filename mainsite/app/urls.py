from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardPage , name="dashboard"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
]