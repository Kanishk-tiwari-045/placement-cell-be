# models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
import random
import datetime

class Organization(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    registration_number = models.CharField(max_length=50, unique=True)
    founded_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    industry_type = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def generate_otp(self):
        self.otp = ''.join(random.choices('0123456789', k=6))
        self.otp_created_at = timezone.now()
        self.save()

    def is_otp_valid(self, otp):
        if self.otp == otp and (timezone.now() - self.otp_created_at) < datetime.timedelta(minutes=10):
            return True
        return False

    def __str__(self):
        return self.name
