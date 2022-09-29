from django.shortcuts import render

from flight.serializers import FlightSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
   
