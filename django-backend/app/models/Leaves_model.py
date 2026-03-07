from django.db import models
from django.apps import apps
from employee.models import Employee

class Leaves(models.Model):
    LEAVE_TYPES = [
        ('Sick', 'Sick Leave'),
        ('Casual', 'Casual Leave'),
        ('Annual', 'Annual Leave'),
        ('Maternity', 'Maternity Leave'),
        ('Unpaid', 'Unpaid Leave'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type} - {self.status}"

    def save(self, *args, **kwargs):
        LeaveBalance = apps.get_model("app", "LeaveBalance")

        # Calculate leave duration
        leave_days = (self.end_date - self.start_date).days + 1

        if self.status == 'Approved':
            leave_balance, _ = LeaveBalance.objects.get_or_create(
                employee=self.employee,
                leave_type=self.leave_type,
                defaults={'total_leaves': 0, 'used_leaves': 0}
            )

            if leave_balance.remaining_leaves >= leave_days:
                leave_balance.used_leaves += leave_days
                leave_balance.save()
            else:
                self.status = "Rejected"

        super().save(*args, **kwargs)
