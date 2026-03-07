from django.contrib import admin
from app.models import Reimbursement
from unfold.admin import ModelAdmin

@admin.register(Reimbursement)
class ReimbursementAdmin(ModelAdmin):
    list_display = ("expense", "reimbursed", "reimbursed_on")
    search_fields = ("expense__travel_request__employee__username",)
    list_filter = ("reimbursed",)