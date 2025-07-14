from django.contrib import admin
from attendance.models import AttendanceRegister, AttendanceImage
from unfold.admin import ModelAdmin

class AttendanceImageInline(admin.TabularInline):
    model = AttendanceImage
    extra = 3
    min_num = 1
    max_num = 10 

@admin.register(AttendanceRegister)
class AttendanceRegisterAdmin(ModelAdmin):
    list_display = ('username', 'employee')
    inlines = [AttendanceImageInline]