from django.contrib import admin 
from employee.models import Department
from unfold.admin import ModelAdmin

@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = ("name" , "description")
    search_fields = ("name" , "description")
    list_filter = ("name", "description")
    list_per_page = 10

   