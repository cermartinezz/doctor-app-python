from datetime import date

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from appointments.serializers import AppointmentSerializer
from patients.models import Patient, Insurance, MedicalRecord


class PatientSerializer(ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)
    age = SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            'appointments',
            'age'
        ]

    def get_age(self, patient):
        age_time_delta = date.today() - patient.date_of_birth
        years = age_time_delta.days // 365  # Return age in years
        return f"{years} years"




class InsuranceSerializer(ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"

class MedicalRecordsSerializer(ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"