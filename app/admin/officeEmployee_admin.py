from django.contrib import admin 
from app.models import Employee
from unfold.admin import ModelAdmin

@admin.register(Employee)
class OfficeEmployeeAdmin(ModelAdmin):
    list_display = ("employee_id", "name" , "email","designation" , "salary" , "employment_status")
    search_fields = ("employee_id", "name" , "email" , "phone", "designation", "salary", "employment_status")
    list_filter = ("employment_status", "designation")
    list_per_page = 10
<<<<<<< HEAD
=======

>>>>>>> 34accc8f6043820424f9169cdc62545edc287931
