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

@api_view(['GET','PUT'])
def patient_detail_view(request, id):
    if request.method == 'GET':
        patient = Patient.objects.filter(id=id).first()
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == 'PUT':
        patient = Patient.objects.filter(id=id).first()
        if patient is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
