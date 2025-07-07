from django.contrib import admin
from app.models import TravelRequest
from unfold.admin import ModelAdmin

@admin.register(TravelRequest)
class TravelRequestAdmin(ModelAdmin):
    list_display = (
        "employee",
        "destination",
        "purpose",
        "start_date",
        "end_date",
        "status",
    )
    search_fields = ("employee__username", "destination")
    list_filter = ("status",)