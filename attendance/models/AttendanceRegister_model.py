from django.db import models
from employee.models import Employee


def upload_to_username_folder(instance, filename):
    username = instance.username  # Use the username entered manually
    return f"attendance/{username}/{filename}"

class AttendanceRegister(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)  # Manually entered username
    image = models.ImageField(upload_to=upload_to_username_folder)

    def __str__(self):
        return f"{self.username} - {self.image.name}"
    
