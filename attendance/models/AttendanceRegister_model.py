from django.db import models
from employee.models import Employee

def upload_to_username_folder(instance, filename):
    username = instance.attendance.username  # Use the username entered manually
    return f"attendance/{username}/{filename}"

class AttendanceRegister(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class AttendanceImage(models.Model):
    attendance = models.ForeignKey(AttendanceRegister, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to_username_folder)

    def __str__(self):
        return f"{self.attendance.username} - {self.image.name}"
