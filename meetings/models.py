from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nazwa sali
    capacity = models.IntegerField()  # Pojemność sali

    def __str__(self):
        return self.name

class Meeting(models.Model):
    title = models.CharField(max_length=255)  # Tytuł spotkania
    description = models.TextField()  # Opis spotkania
    start_datetime = models.DateTimeField()  # Data i godzina rozpoczęcia
    end_datetime = models.DateTimeField()    # Data i godzina zakończenia
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='meetings')  # Sala konferencyjna
    participants = models.ManyToManyField(User, related_name='meetings')  # Uczestnicy spotkania

    def __str__(self):
        return self.title

    def is_in_conflict(self):
        # Sprawdzanie konfliktu z innym spotkaniem w tej samej sali
        conflicting_meetings = Meeting.objects.filter(
            room=self.room,
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime
        )
        return conflicting_meetings.exists()

    def is_user_available(self, user):
        # Sprawdzanie, czy użytkownik jest dostępny (czy nie jest na urlopie)
        vacations = user.vacations.filter(
            start_date__lt=self.end_datetime,
            end_date__gt=self.start_datetime,
            status='approved'
        )
        return not vacations.exists()
