from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Offer(models.Model):
    departure = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    seats_available = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    price = models.IntegerField(default=0)
    by = models.ForeignKey(User, on_delete=models.CASCADE)


class Request(models.Model):
    provider = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='provider')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    pro = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pro', default=2)
    pickup_location = models.CharField(max_length=150)
    seats_required = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    description = models.TextField()
    approved = models.BooleanField(default=False, blank=True)
    z = models.IntegerField(default=0, blank=True)
