from django.contrib import admin
from app.models import Leaves
from unfold.admin import ModelAdmin

@admin.register(Leaves)
class LeavesAdmin(ModelAdmin):
    list_display = ("employee", "leave_type", "start_date", "end_date", "status")
    search_fields = ("employee__username",)
    list_filter = ("leave_type", "status")
