from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    # pass
    # chambres= Chambre.objects.all()
    # catalogues= Catalogue.objects.all()
    # testimonials = Testimonial.objects.all()
    render(request, 'index.html', {'testimonial': 'test'})
    render(request, 'index.html', {'catalogues': 'test'})
    return render(request, "index.html", {'chambres': 'test'})


def reservation(request):
    return render(request, "reservation.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    # chambres = Chambre.objects.all()
    return render(request, "blog.html", {'chambres': 'test'})


def about(request):
    return render(request, 'about.html')


def hotels(request):
    return render(request, 'hotels.html')


def hotel(request):
    return render(request, 'hotel.html')
