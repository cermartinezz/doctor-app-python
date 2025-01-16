from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


# Create your views here.
class ListAppointmentView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DetailAppointmentView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer