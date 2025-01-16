from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


# Create your views here.
class ListAppointmentView(ListCreateAPIView):
    """
    List all appointments or create a new appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DetailAppointmentView(ListCreateAPIView):
    """
    Retrieve, update or delete an appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer