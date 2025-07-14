from django.contrib import admin
from django import forms
from attendance.models import AttendanceRegister
from django.forms.widgets import ClearableFileInput


@admin.register(AttendanceRegister)
class AttendanceRegisterAdmin(admin.ModelAdmin):
    list_display = ('employee', 'username')
    search_fields = ('employee__name', 'username')

    def save_model(self, request, obj, form, change):
        files = request.FILES.getlist('image')
        employee = form.cleaned_data.get('employee')
        username = form.cleaned_data.get('username')

        if files:
            # Create a separate AttendanceRegister record for each image
            for f in files:
                AttendanceRegister.objects.create(employee=employee, username=username, image=f)
        else:
            # fallback to default save if no files uploaded
            super().save_model(request, obj, form, change)
