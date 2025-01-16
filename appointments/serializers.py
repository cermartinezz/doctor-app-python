from rest_framework.serializers import ModelSerializer

from appointments.models import Appointment, MedicalNote


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
class MedicalNoteSerializer(ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"