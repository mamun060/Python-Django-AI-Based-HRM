from django.contrib import admin 
from app.models import OfficeEmployee

class OfficeEmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "name" , "email","designation" , "salary" , "employment_status")
    search_fields = ("employee_id", "name" , "email" , "phone", "designation", "salary", "employment_status")
    list_filter = ("employment_status", "designation")
    list_per_page = 2
admin.site.register(OfficeEmployee, OfficeEmployeeAdmin)