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

    def get_fields(self, request, obj=None):
        fields = ['employee']
        if obj:  # Only show username when editing
            fields.append('username')
        return fields

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Make username read-only when editing
            return ['username']
        return []