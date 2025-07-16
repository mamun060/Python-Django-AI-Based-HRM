from django.db import models
from employee.models import Employee

class DailyAttendanceSummary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.employee.username} - {self.date}"

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']
