from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    job_title = models.CharField(max_length=150)
    image_user = models.ImageField(upload_to='image_user/', null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Administrator'),
        ('user', 'User'),
        ('manager', 'Manager'),
    ], default='user')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


class Company(models.Model):
    name_company = models.CharField(max_length=32)
    registration_number_company = models.PositiveSmallIntegerField()
    address_company = models.TextField()
    industry = models.TextField()