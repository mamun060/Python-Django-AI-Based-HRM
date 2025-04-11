from django.db import models
from django.contrib.auth.models import User

class TravelRequest(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    purpose = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    requested_on = models.DateTimeField(auto_now_add=True)