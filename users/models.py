from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.is_active = True 
        user.username = phone_number
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number,password=None, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.is_active = True  
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True) 
    password = models.CharField(max_length=128, blank=True) # For SuperUser Only
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_usable_password(self):
        if self.is_superuser:
            return super().has_usable_password()
        else:
            return False
