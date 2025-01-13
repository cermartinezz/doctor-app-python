from django.db import models
from django.db.models import Model


class Doctor(Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()

class Department(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class DoctorAvailability(Model):
    doctor = models.ForeignKey(Doctor, related_name='availabilities', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.TimeField()

class MedicalNote(Model):
    doctor = models.ForeignKey(Doctor, related_name='medical_notes', on_delete=models.CASCADE)
    node = models.TextField()
    date = models.DateField
