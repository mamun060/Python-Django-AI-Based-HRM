from django.db import models
from employee.models import Employee

class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20)
    total_leaves = models.IntegerField()
    used_leaves = models.IntegerField(default=0)
    remaining_leaves = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Auto-calculate remaining leaves
        self.remaining_leaves = self.total_leaves - self.used_leaves
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type} - {self.remaining_leaves} Remaining"
