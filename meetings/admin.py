from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')  # Wyświetlanie kolumn w panelu admina
    search_fields = ('name',)  # Możliwość wyszukiwania po nazwie sali

admin.site.register(Room, RoomAdmin)
