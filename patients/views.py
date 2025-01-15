from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from patients.models import Patient
from patients.serializers import PatientSerializer

@api_view(['GET','POST'])
def patient_list_view(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def patient_detail_view(request, id):
    patient = Patient.objects.filter(id=id).first()
    if patient is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        patient.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

