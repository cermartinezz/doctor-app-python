from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.models import Patient
from patients.serializers import PatientSerializer


class ListPatientsView(APIView):
    allow_methods = ['GET','POST']

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetailPatientView(APIView):
    allowed_methods = ['GET','PUT','DELETE']

    def get(self, request, id):
        patient = Patient.objects.filter(id=id).first()
        if patient is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, id):
        patient = Patient.objects.filter(id=id).first()
        if patient is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        patient = Patient.objects.filter(id=id).first()
        if patient is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

