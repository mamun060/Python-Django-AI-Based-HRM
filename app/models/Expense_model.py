from django.db import models
from employee.models import Employee 
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

EXPENSE_TYPE_CHOICES = [
    ('travel', 'Travel'),
    ('office_supplies', 'Office Supplies'),
    ('entertainment', 'Client Entertainment'),
    ('training', 'Training'),
    ('other', 'Other'),
]

class Expense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # This is the expense name/title
    expense_type = models.CharField(max_length=50, choices=EXPENSE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.FileField(upload_to='receipts/', validators=[validate_file_extension])
    description = models.TextField(blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  