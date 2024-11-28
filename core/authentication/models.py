from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=255,blank=True, null=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    domain = models.URLField(blank=True, null=True)
    year_founded = models.CharField(max_length=255,blank=True, null=True)
    industry = models.CharField(max_length=255,blank=True, null=True)
    size_range = models.CharField(max_length=100,blank=True, null=True)
    locality = models.CharField(max_length=255,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    current_employee_estimate = models.CharField(max_length=255,blank=True, null=True)
    total_employee_estimate = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name