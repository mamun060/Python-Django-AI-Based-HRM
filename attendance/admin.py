from django.contrib import admin
from .models import AttendanceRecord
from unfold.admin import ModelAdmin

# Register your models here
@admin.register(AttendanceRecord)
class AttendanceAdmin(ModelAdmin):
    list_display = ('name', 'time', 'accuracy', 'image')
    search_fields = ('name', 'time', 'accuracy')
    list_filter = ('name', 'time')
    ordering = ('-time',)
    list_per_page = 20
