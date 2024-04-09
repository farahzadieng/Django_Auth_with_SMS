from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, code, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.is_active = False  # Set user inactive until verified
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)  # Adjust length for your phone number format
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_usable_password(self):
        return False  # Override as we don't use a password field

