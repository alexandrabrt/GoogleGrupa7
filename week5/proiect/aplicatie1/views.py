from django.shortcuts import render
from django.views.generic import ListView
from aplicatie1.models import Location


# Create your views here.
class LocationView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'
