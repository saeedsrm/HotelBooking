from django.db import models
from accounts.models import Account
from hotels.models import *


class Comment(models.Model):
    account = models.CharField(max_length=200)
    is_confirmed = models.BooleanField(default=False)
    note = models.TextField(verbose_name="comment")
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)


class Reservation(models.Model):
    account = models.CharField(max_length=200)
    Date_Check_In = models.DateField(auto_now=False)
    Date_Check_Out = models.DateField(auto_now=False)
    number_person = models.IntegerField(default=0)
    Note = models.TextField()

    def __str__(self):
        return self.Name


class contactUs(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField()
    note = models.TextField()
