from django.urls import path
from . import views

urlpatterns = [
    # Przykładowa ścieżka do widoku urlopów
    path('', views.index, name='vacations_index'),
]
