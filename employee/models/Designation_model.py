from django.db import models
from employee.models import JobType, Department

class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name