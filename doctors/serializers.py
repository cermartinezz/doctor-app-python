from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from doctors.models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_email(self, value):
        if "@example.com" in value:
            return value

        raise ValidationError("Email is not from example.com")

    def validate(self, data):
        if len(data['contact_number']) <= 9 and data['is_on_vacation']:
            raise ValidationError("Contact number is required and valid when doctor is on vacation")

        return super().validate(data)


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class DoctorAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"

class MedicalNoteSerializer(ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"