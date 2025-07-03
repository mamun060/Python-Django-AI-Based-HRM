from django.contrib import admin
from app.models import Attendance
from unfold.admin import ModelAdmin

@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    list_display = ('id', 'employee', 'date', 'status')
    search_fields = ('employee__name',)
    list_filter = ('status', 'date')
    ordering = ('-date',)
    list_per_page = 20
