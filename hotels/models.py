from django.db import models


class hotel(models.Model):
    name = models.CharField(max_length=100, )
    info = models.TextField()
    address = models.CharField(max_length=300, )
    score = models.IntegerField()
    stars = models.IntegerField()
    is_suspend = models.BooleanField(default=False)


class room(models.Model):
    room_number = models.CharField(max_length=100, )
    photo = models.FileField(upload_to='pics/', default='pics/room3.jpg')
    discription = models.TextField()
    cost = models.IntegerField()
    capacity = models.IntegerField()
    is_empty = models.BooleanField(default=True)
