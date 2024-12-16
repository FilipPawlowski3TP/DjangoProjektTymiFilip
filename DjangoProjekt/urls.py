from django.contrib import admin
from django.urls import path, include  # Dodaj include, jeśli chcesz używać url w aplikacjach

urlpatterns = [
    # Ścieżka do panelu admina
    path('admin/', admin.site.urls),  # Ścieżka do panelu admina

    # Ścieżki do aplikacji
    path('meetings/', include('meetings.urls')),  # Ścieżka do aplikacji meetings
    path('vacations/', include('vacations.urls')),  # Ścieżka do aplikacji vacations
]
