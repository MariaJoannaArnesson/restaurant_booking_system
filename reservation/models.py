from django.db import models
from django.contrib.auth.models import User
import datetime


class No_of_guest(models.Model):
    guest = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.guest)


class OnlineBooking(models.Model):

    TIME_CHOICES = [
        ("6 PM", "6 PM"),
        ("6:30 PM", "6:30 PM"),
        ("7 PM", "7 PM"),
        ("7:30 PM", "7:30 PM"),
        ("8 PM", "8 PM"),
        ("8:30 PM", "8:30 PM"),
        ("9 PM", "9 PM"),
        ("9:30 PM", "9:30 PM"),
        ("10 PM", "10 PM"),
        ("10:30 PM", "10:30 PM"),
    ]

    OCCASSION_CHOICES = [
        ("Birthday", "Birthday"),
        ("Anniversary", "Anniversary"),
        ("Date night ", "Date night "),
        ("Business Meal", "Business Meal"),
        ("Other", "Other"),
        ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_booking'
    )
    no_of_guest = models.ForeignKey(No_of_guest, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.CharField(null=True, blank=False, choices=TIME_CHOICES, max_length=60)
    occassion = models.CharField(max_length=150, choices=OCCASSION_CHOICES, default="Birthday")
    special_request = models.TextField(max_length=300, blank=True)

    class Meta:
        unique_together = ["no_of_guest", "date", "time"]

    def __str__(self):
        return f'{self.date}'
