from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class Details(models.Model):
    Address=models.CharField(max_length=50,null=True,blank=True)
    Phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        self.Address


class Employeedb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    employee_code = models.CharField(max_length=10, unique=True, null=True, blank=True)  # New field for unique code
    email = models.EmailField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # First save without employee_code to generate the instance ID
        super(Employeedb, self).save(*args, **kwargs)

        # Now generate the employee code if it hasn't been set
        if not self.employee_code:
            self.employee_code = f"EMP{self.id:04d}"  # Format employee code as EMP0001, EMP0002, etc.
            self.save(update_fields=['employee_code'])  # Update the employee_code field without overwriting the rest

    def __str__(self):
        return self.name
class Servicedb(models.Model):
    service = models.CharField(max_length=50, null=True, blank=True)
    description=models.CharField(max_length=150, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        self.service


