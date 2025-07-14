from django.db import models

# Create your models here.
class AttendanceRecord(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    accuracy = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='attendance_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.time.strftime('%Y-%m-%d %H:%M:%S')} - {self.accuracy:.2f}%"
    class Meta: 
        verbose_name = "Attendance Record"
        verbose_name_plural = "Attendance Records"
        ordering = ['-time']
