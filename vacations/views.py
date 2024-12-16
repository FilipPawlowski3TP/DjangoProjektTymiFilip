# vacations/views.py

from django.shortcuts import render

# Widok główny aplikacji Vacations
def index(request):
    return render(request, 'vacations/index.html')  # Renderowanie szablonu index.html
