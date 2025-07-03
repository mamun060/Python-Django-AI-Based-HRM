from django.db import models
from django.contrib.auth.models import User

class LeaveBalance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20)
    total_leaves = models.IntegerField()
    used_leaves = models.IntegerField(default=0)
    remaining_leaves = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} - {self.remaining_leaves} Remaining"
