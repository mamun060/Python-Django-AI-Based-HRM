# churn_prediction/forms.py
from django import forms
from .models import EmployeeInput

class EmployeeInputForm(forms.ModelForm):
    class Meta:
        model = EmployeeInput
        fields = '__all__'
        widgets = {
            'age': forms.NumberInput(attrs={'min': 18, 'max': 65}),
            'gender': forms.Select(),
            'satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5}),
            'work_hours': forms.NumberInput(attrs={'min': 0}),
            'relationship_satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5}),
            'environment_satisfaction': forms.NumberInput(attrs={'step': 0.1, 'min': 1, 'max': 5}),
            'overtime': forms.Select(),
            'education_background': forms.Select(choices=[
                ('Marketing', 'Marketing'),
                ('Life Sciences', 'Life Sciences'),
                ('Human Resources', 'Human Resources'),
                ('Medical', 'Medical'),
                ('Other', 'Other'),
                ('Technical Degree', 'Technical Degree'),
            ]),
            'emp_department': forms.Select(choices=[
                ('Sales', 'Sales'),
                ('Human Resources', 'Human Resources'),
                ('Development', 'Development'),
                ('Data Science', 'Data Science'),
                ('Research & Development', 'Research & Development'),
                ('Finance', 'Finance'),
            ]),
            'emp_job_role': forms.Select(choices=[
                ('Sales Executive', 'Sales Executive'),
                ('Manager', 'Manager'),
                ('Developer', 'Developer'),
                # Add all job roles here...
            ]),
            'distance_from_home': forms.NumberInput(),
            'emp_education_level': forms.TextInput(),
            'emp_job_involvement': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'emp_last_salary_hike_percent': forms.NumberInput(attrs={'min': 0}),
            'total_work_experience_in_years': forms.NumberInput(attrs={'min': 0}),
        }
