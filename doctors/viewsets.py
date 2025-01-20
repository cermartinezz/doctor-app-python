from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from appointments.serializers import AppointmentSerializer
from doctors.models import Doctor, Department, DoctorAvailability, MedicalNote
from doctors.permissions import IsDoctor
from doctors.serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer


class DoctorViewSet(ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        data = request.data.copy()
        data['doctor'] = doctor.id

        if request.method == 'POST':
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = doctor.appointments.all()

            return Response(AppointmentSerializer(appointments, many=True).data)


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