from django.contrib import admin 
from employee.models import Designation
from unfold.admin import ModelAdmin

@admin.register(Designation)
class PositionAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 10

   