from django.contrib import admin 
from employee.models import Employee
from unfold.admin import ModelAdmin

@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = (
        "name", "email", "phone", 
        "department", "position", "job_type", 
        "salary", "employment_status"
    )
    search_fields = (
        "employee_id", "name", "email", "phone", 
        "department__name", "position__name", "job_type__name"
    )
    list_filter = (
        "employment_status", "department", "position", "job_type"
    )
    list_per_page = 10

    fieldsets = (
        ('Basic Info', {
            'fields': (
                ('employee_id', 'name'),
                ('email', 'phone'),
            )
        }),
        ('Job Details', {
            'fields': (
                ('department', 'position'),
                ('job_type', 'salary'),
                ('employment_status', 'joining_date')
            )
        }),
        ('Address Info', {
            'fields': (
                ('present_address', 'permanent_address'),
            )
        }),
        ('Documents & Media', {
            'fields': (
                ('employee_photo', 'employee_doc'),
            )
        }),
    )