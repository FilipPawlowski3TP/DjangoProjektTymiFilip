# meetings/views.py

from django.shortcuts import render

# Widok główny aplikacji Meetings
def index(request):
    return render(request, 'meetings/index.html')  # Renderuje szablon index.html
