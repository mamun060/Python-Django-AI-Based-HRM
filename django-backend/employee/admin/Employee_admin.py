from django.contrib import admin
from ..models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "name" , "email","position" , "salary" , "employment_status")
    search_fields = ("employee_id", "name" , "email" , "phone", "position", "salary", "employment_status")
    list_filter = ("employment_status", "position")
    list_per_page = 10
