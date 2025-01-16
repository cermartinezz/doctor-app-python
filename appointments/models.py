from django.db import models
from django.db.models import Model

from doctors.models import Doctor
from patients.models import Patient


class Appointment(Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=20)

class MedicalNote(Model):
    appointment = models.ForeignKey(Appointment, related_name='medical_notes', on_delete=models.CASCADE)
    node = models.TextField()
    date = models.DateField()
