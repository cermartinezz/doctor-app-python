from rest_framework.viewsets import ModelViewSet

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()