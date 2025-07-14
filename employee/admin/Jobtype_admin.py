from django.contrib import admin 
from employee.models import JobType
from unfold.admin import ModelAdmin

@admin.register(JobType)
class JobTypeAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 10

   