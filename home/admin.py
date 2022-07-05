from django.contrib import admin
from home.models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'account', 'is_confirmed', 'note')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'account', 'Date_Check_In', 'Date_Check_Out', 'number_person', 'Note')
