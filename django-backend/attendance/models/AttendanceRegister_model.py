import re
from django.db import models
from employee.models import Employee

def upload_to_username_folder(instance, filename):
    username = instance.attendance.username  # Use the username entered manually
    return f"attendance/{username}/{filename}"

class AttendanceRegister(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True, blank=True)

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # Auto-generate username if not provided
        if not self.username and self.employee:
            # Sanitize employee name
            base = re.sub(r'[^a-zA-Z0-9_-]', '', self.employee.name.replace(" ", "_")).lower()
            username = f"{base}_{self.employee.id}"
            counter = 1

            # Ensure uniqueness
            while AttendanceRegister.objects.filter(username=username).exists():
                username = f"{base}_{counter}"
                counter += 1

            self.username = username

        super().save(*args, **kwargs)

class AttendanceImage(models.Model):
    attendance = models.ForeignKey(AttendanceRegister, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to_username_folder)

    def __str__(self):
        return f"{self.attendance.username} - {self.image.name}"
