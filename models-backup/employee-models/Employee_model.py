from django.db import models
from employee.models import JobType, Department, Designation

class Employee(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('full_time', 'Full Time'),
        ('permanent', 'Permanent'),
        ('intern', 'Intern'),
        ('part_time', 'Part Time'),
        ('contract_base', 'Contract Base'),
    ]

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25, unique=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    employment_status = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_STATUS_CHOICES,
        default='full_time'
    )
    employee_photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    employee_doc = models.FileField(upload_to='employee_docs/', blank=True, null=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"