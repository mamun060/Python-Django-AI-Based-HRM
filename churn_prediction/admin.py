from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import EmployeeInput
from .forms import EmployeeInputForm
from .predict import predict_employee_status  # your custom prediction function

class EmployeeInputAdmin(ModelAdmin):
    list_display = ('id', 'age', 'gender', 'emp_job_role', 'satisfaction', 'predicted_churn')
    list_filter = ('gender', 'emp_department', 'emp_job_role', 'overtime')

    fieldsets = (
        ('Basic Info', {
            'fields':  (
            ('employee', 'age'),
            ('gender', 'emp_job_role'),
            ('emp_department',),
        ),
            'classes': ('unfold',),
        }),
        ('Job Satisfaction', {
            'fields': (
                ('satisfaction', 'work_hours'),
                ('relationship_satisfaction', 'environment_satisfaction'),
            ),
            'classes': ('unfold',),
        }),
        ('Additional Details', {
            'fields': (
                (
                    'overtime', 'education_background'
                ),
                (
                    'distance_from_home', 'emp_education_level'
                ),
                (
                    'emp_job_involvement', 'emp_last_salary_hike_percent', 'total_work_experience_in_years'
                ),
                (
                    'predicted_churn'
                )
            ),
            'classes': ('unfold',),
        }),
    )

    readonly_fields = ('predicted_churn',)

    def save_model(self, request, obj, form, change):
        # Assuming you have a predict_employee_status function defined elsewhere
        obj.predicted_churn = predict_employee_status(obj)
        super().save_model(request, obj, form, change)

admin.site.register(EmployeeInput, EmployeeInputAdmin)