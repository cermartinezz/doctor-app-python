from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from doctors.models import Doctor, Department, DoctorAvailability, MedicalNote
from doctors.permissions import IsDoctor
from doctors.serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer


class DoctorViewSet(ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DepartmentViewSet(ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DoctorAvailabilityViewSet(ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class MedicalNoteViewSet(ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()