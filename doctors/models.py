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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Department(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class DoctorAvailability(Model):
    doctor = models.ForeignKey(Doctor, related_name='availabilities', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.doctor.first_name} {self.doctor.last_name} - {self.start_date} {self.start_time}'

class MedicalNote(Model):
    doctor = models.ForeignKey(Doctor, related_name='medical_notes', on_delete=models.CASCADE)
    node = models.TextField()
    date = models.DateField

    def __str__(self):
        return f'{self.doctor.first_name} {self.doctor.last_name} - {self.date}'
