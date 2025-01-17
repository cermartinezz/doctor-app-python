from rest_framework.viewsets import ModelViewSet

from patients.models import Patient, Insurance, MedicalRecord
from patients.serializers import PatientSerializer, InsuranceSerializer, MedicalRecordsSerializer


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class InsuranceViewSet(ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordsSerializer
    queryset = MedicalRecord.objects.all()