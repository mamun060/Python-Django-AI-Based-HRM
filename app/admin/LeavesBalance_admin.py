from django.contrib import admin
from app.models import LeaveBalance
from unfold.admin import ModelAdmin

@admin.register(LeaveBalance)
class LeaveBalanceAdmin(ModelAdmin):
    pass