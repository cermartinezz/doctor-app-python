from rest_framework.serializers import ModelSerializer
from patients.models import Patient, Insurance, MedicalRecord


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class InsuranceSerializer(ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"

class MedicalRecordsSerializer(ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"