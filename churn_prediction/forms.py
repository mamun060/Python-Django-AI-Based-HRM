# churn_prediction/forms.py

from django import forms
from .models import EmployeeInput

class EmployeeInputForm(forms.ModelForm):
    class Meta:
        model = EmployeeInput
        fields = '__all__'
        widgets = {
            'age': forms.NumberInput(attrs={'min': 18, 'max': 65, 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5, 'class': 'form-control'}),
            'work_hours': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'relationship_satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5, 'class': 'form-control'}),
            'environment_satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5, 'class': 'form-control'}),
            'overtime': forms.Select(attrs={'class': 'form-control'}),
            'education_background': forms.Select(choices=[
                ('Marketing', 'Marketing'),
                ('Life Sciences', 'Life Sciences'),
                ('Human Resources', 'Human Resources'),
                ('Medical', 'Medical'),
                ('Other', 'Other'),
                ('Technical Degree', 'Technical Degree'),
            ], attrs={'class': 'form-control'}),
            'emp_department': forms.Select(choices=[
                ('Sales', 'Sales'),
                ('Human Resources', 'Human Resources'),
                ('Development', 'Development'),
                ('Data Science', 'Data Science'),
                ('Research & Development', 'Research & Development'),
                ('Finance', 'Finance'),
            ], attrs={'class': 'form-control'}),
            'emp_job_role': forms.Select(choices=[
                ('Sales Executive', 'Sales Executive'),
                ('Manager', 'Manager'),
                ('Developer', 'Developer'),
                # Add all job roles...
            ], attrs={'class': 'form-control'}),
            'distance_from_home': forms.NumberInput(attrs={'class': 'form-control'}),
            'emp_education_level': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_job_involvement': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'emp_last_salary_hike_percent': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'total_work_experience_in_years': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
        }
