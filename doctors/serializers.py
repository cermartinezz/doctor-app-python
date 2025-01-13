from rest_framework.serializers import ModelSerializer

from doctors.models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

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