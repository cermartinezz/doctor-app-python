from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status

from doctors.models import Doctor
from patients.models import Patient


# Create your tests here.
class DoctorViewTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.patient = Patient.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            date_of_birth=self.fake.date_of_birth(),
            contact_number=self.fake.phone_number(),
            email=self.fake.email(),
            address=self.fake.address(),
            medical_history=self.fake.text(),
        )
        self.doctor = Doctor.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            qualification=self.fake.job(),
            contact_number=self.fake.phone_number(),
            email=self.fake.email(domain='example.com'),
            address=self.fake.address(),
            biography=self.fake.text(),
            is_on_vacation=self.fake.boolean(),
        )

    def test_guest_user_gets_403(self):
        url = reverse('doctor-appointments', kwargs={
            'pk': self.doctor.id
        })

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


