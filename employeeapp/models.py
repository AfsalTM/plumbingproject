from django.db import models

# Create your models here.
class signindb(models.Model):
    employee_code = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    subscription_type = models.CharField(max_length=50, null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)