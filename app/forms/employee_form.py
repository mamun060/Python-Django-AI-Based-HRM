from django import forms
from app.models import OfficialDocument

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = OfficialDocument
        fields = [
            'name', 
            'email', 
            'phone', 
            'designation', 
            'present_address', 
            'permanent_address', 
            'department', 
            'salary', 
            'joining_date', 
            'employment_status', 
            'employee_photo', 
            'employee_doc'
        ]