from django.db import models
from django.contrib.auth.models import User
from datetime import    datetime, date

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Leave', 'Leave'),
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Present')
    work_hours = models.FloatField(default=0)
    overtime_hours = models.FloatField(default=0)
    late_entry_approved = models.BooleanField(default=False)
    early_leave_approved = models.BooleanField(default=False)

    def calculate_work_hours(self):
        if self.check_in and self.check_out:
            delta = datetime.combine(date.min, self.check_out) - datetime.combine(date.min, self.check_in)
            self.work_hours = delta.total_seconds() / 3600  # Convert to hours
        else:
            self.work_hours = 0

    def __str__(self):
        return f"{self.employee.username} - {self.date} - {self.status}"
