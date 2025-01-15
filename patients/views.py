from django.contrib.admin.utils import lookup_field
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.models import Patient
from patients.serializers import PatientSerializer


class ListPatientsView(ListAPIView, CreateAPIView):
    allow_methods = ['GET','POST']
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

