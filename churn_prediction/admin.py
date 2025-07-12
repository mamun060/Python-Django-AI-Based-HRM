from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import EmployeeInput
from .forms import EmployeeInputForm
from .predict import predict_employee_status  # your custom prediction function

class EmployeeInputAdmin(ModelAdmin):
    form = EmployeeInputForm

    list_display = ('id', 'age', 'gender', 'emp_job_role', 'satisfaction', 'predicted_churn')
    list_filter = ('gender', 'emp_department', 'emp_job_role', 'overtime')

    # Use fieldsets with unfold panels for nice collapsible sections
    fieldsets = (
        ('Basic Info', {
            'fields': ('age', 'gender', 'emp_job_role', 'emp_department'),
            'classes': ('unfold',),  # This will make this section collapsible
        }),
        ('Job Satisfaction', {
            'fields': ('satisfaction', 'work_hours', 'relationship_satisfaction', 'environment_satisfaction'),
            'classes': ('unfold',),
        }),
        ('Additional Details', {
            'fields': ('overtime', 'education_background', 'distance_from_home', 'emp_education_level', 
                       'emp_job_involvement', 'emp_last_salary_hike_percent', 'total_work_experience_in_years', 'predicted_churn'),
            'classes': ('unfold',),
        }),
    )

    readonly_fields = ('predicted_churn',)  # Prevent editing predicted field manually

    def save_model(self, request, obj, form, change):
        # Run prediction on save and store result
        obj.predicted_churn = predict_employee_status(obj)
        super().save_model(request, obj, form, change)

admin.site.register(EmployeeInput, EmployeeInputAdmin)
