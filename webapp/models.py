from django.db import models
import uuid
class bookingdb(models.Model):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)  # New date field
    job_code = models.CharField(max_length=10, unique=True, editable=False,null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate a random job code if not already set
        if not self.job_code:
            self.job_code = self.generate_job_code()
        super().save(*args, **kwargs)

    def generate_job_code(self):
        # Generate a unique job code by checking for duplicates
        while True:
            job_code = str(uuid.uuid4())[:8]  # Generate an 8-character random code
            if not bookingdb.objects.filter(job_code=job_code).exists():  # Check if job code is unique
                return job_code
    def __str__(self):
        self.user_name


class Enquiry(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    date = models.DateField()
    request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
class PlumberPartner(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    employee_code = models.CharField(max_length=10, unique=True)  # Unique employee code
    email = models.EmailField()

    def __str__(self):
        return self.name