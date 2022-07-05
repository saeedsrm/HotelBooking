from django.contrib import admin
from hotels.models import *


@admin.register(hotel)
class hotelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'info', 'score', 'stars', 'is_suspend')


@admin.register(room)
class roomAdmin(admin.ModelAdmin):
    list_display = (
        'room_number', 'discription', 'cost', 'capacity', 'is_empty')


@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = (
        'photo', 'note')
