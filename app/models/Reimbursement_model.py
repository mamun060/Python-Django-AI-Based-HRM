from django.db import models
from app.models import Expense

class Reimbursement(models.Model):
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE)
    reimbursed = models.BooleanField(default=False)
    reimbursed_on = models.DateField(null=True, blank=True)