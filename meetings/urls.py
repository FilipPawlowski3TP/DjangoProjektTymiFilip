from django.urls import path
from . import views

urlpatterns = [
    # Przykładowa ścieżka do widoku spotkania
    path('', views.index, name='meetings_index'),
]
