from django.contrib import admin
from app.models import LeaveBalance
from unfold.admin import ModelAdmin

@admin.register(LeaveBalance)
class LeaveBalanceAdmin(ModelAdmin):
<<<<<<< HEAD
    pass
=======
    list_display = (
        "employee",
        "leave_type",
        "total_leaves",
        "used_leaves",
        "remaining_leaves",
    )
    search_fields = ("employee__username",)
    list_filter = ("leave_type",)
>>>>>>> 34accc8f6043820424f9169cdc62545edc287931
