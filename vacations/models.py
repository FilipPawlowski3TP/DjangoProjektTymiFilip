from django.db import models
from django.contrib.auth.models import User


class Vacation(models.Model):
    VACATION_TYPE_CHOICES = [
        ('vacation', 'Wakacje'),
        ('sick', 'Choroba'),
        ('personal', 'Sprawy prywatne'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Oczekujący'),
        ('approved', 'Zatwierdzony'),
        ('rejected', 'Odrzucony'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacations')  # Użytkownik, który bierze urlop
    start_date = models.DateField()  # Data rozpoczęcia urlopu
    end_date = models.DateField()  # Data zakończenia urlopu
    reason = models.CharField(max_length=255, choices=VACATION_TYPE_CHOICES)  # Powód urlopu
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Status urlopu

    def __str__(self):
        return f"Urlop {self.user.username} od {self.start_date} do {self.end_date}"

    def is_approved(self):
        return self.status == 'approved'

    def is_pending(self):
        return self.status == 'pending'

    def is_rejected(self):
        return self.status == 'rejected'
