from django.contrib import admin
from attendance.models import DailyAttendanceSummary 
from unfold.admin import ModelAdmin

@admin.register(DailyAttendanceSummary)
class DailyAttendanceSummaryAdmin(ModelAdmin):
    list_display = ('employee', 'date', 'in_time', 'out_time', 'total_hours')
    list_filter = ('employee', 'date')