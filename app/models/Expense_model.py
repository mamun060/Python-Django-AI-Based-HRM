from django.db import models
from app.models import TravelRequest 

class Expense(models.Model):
    travel_request = models.ForeignKey(TravelRequest, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.FileField(upload_to='receipts/')
    description = models.TextField(blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)