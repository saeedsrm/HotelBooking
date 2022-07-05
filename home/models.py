from django.db import models
from accounts.models import Account


class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    note = models.TextField(verbose_name="comment")


class Reservation(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Date_Check_In = models.DateField(auto_now=False)
    Date_Check_Out = models.DateField(auto_now=False)
    number_person = models.IntegerField(default=0)
    Note = models.TextField()

    def __str__(self):
        return self.Name
