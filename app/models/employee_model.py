from django.db import models
from django.utils.text import slugify

class employeeModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name