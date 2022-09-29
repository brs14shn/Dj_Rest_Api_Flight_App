from django.shortcuts import render
from datetime import datetime, date
from flight.serializers import FlightSerializer,ReservationSerializer,StaffFlightSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .permissions import IsStafforReadOnly
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStafforReadOnly]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer 


    def get_queryset(self):
       now = datetime.now()
       current_time = now.strftime('%H:%M:%S')
       today = date.today()
       if self.request.user.is_staff:
            queryset = super().get_queryset()
            #staff ise hepsini görsün
       else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            #bugünden büyük olanları aldık
            if Flight.objects.filter(date_of_departure=today):
                today_qs =Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                #tarih bugün ve saat kısıtlaması yaptık -->
                queryset = queryset.union(today_qs)
                #<!-- yukarıdaki iki sorguyu birleştirdik. -->
            return queryset  
   
class ReservationView(viewsets.ModelViewSet):
     queryset = Reservation.objects.all()
     serializer_class = ReservationSerializer
     #  reservasyonları kullanıcılara göre kısıtlama
     def get_queryset(self):
       queryset = super().get_queryset()
       if self.request.user.is_staff:
           return queryset
       return queryset.filter(user=self.request.user)  
