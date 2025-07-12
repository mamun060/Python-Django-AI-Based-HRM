# churn_prediction/models.py

from django.db import models

class EmployeeInput(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    OVERTIME_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    satisfaction = models.FloatField()
    work_hours = models.IntegerField()
    relationship_satisfaction = models.FloatField()
    environment_satisfaction = models.FloatField()
    overtime = models.CharField(max_length=5, choices=OVERTIME_CHOICES)
    education_background = models.CharField(max_length=50)
    emp_department = models.CharField(max_length=50)
    emp_job_role = models.CharField(max_length=50)
    distance_from_home = models.FloatField()
    emp_education_level = models.CharField(max_length=10)
    emp_job_involvement = models.FloatField()
    emp_last_salary_hike_percent = models.FloatField()
    total_work_experience_in_years = models.FloatField()
    predicted_churn = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.gender} - {self.emp_job_role}"
