from django.db import models
from .Employee_model import Employee

class Payroll(models.Model):
    PAYROLL_STATUS_CHOICES = [
        ('generated', 'Generated'),
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, choices=PAYROLL_STATUS_CHOICES, default='generated')
    payment_date = models.DateField(blank=True, null=True)

    def calculate_net_salary(self):
        return self.basic_salary + self.allowances - self.deductions

    def save(self, *args, **kwargs):
        self.net_salary = self.calculate_net_salary()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payroll for {self.employee.name} - {self.pay_period_start} to {self.pay_period_end}"
