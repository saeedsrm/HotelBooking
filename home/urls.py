from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='index'),
    path("Reservation", reservation, name='reservation'),
    path("Contact", contact, name='contact'),
    path("Blog", blog, name='blog'),
    path("About", about, name='about'),
    path("hotels", hotels, name='hotels'),
    path("hotel", hotel, name='hotel'),
]
urlpatterns += staticfiles_urlpatterns()
