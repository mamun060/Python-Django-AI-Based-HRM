from django.contrib import admin
from unfold.admin import ModelAdmin
from ..models import Payroll

@admin.register(Payroll)
class PayrollAdmin(ModelAdmin):
    list_display = (
        "employee",
        "pay_period_start",
        "pay_period_end",
        "net_salary",
        "status",
        "payment_date",
    )
    search_fields = ("employee__name",)
    list_filter = ("status", "payment_date")
