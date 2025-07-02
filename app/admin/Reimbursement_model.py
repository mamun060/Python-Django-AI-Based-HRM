from django.contrib import admin
from app.models import Reimbursement
from unfold.admin import ModelAdmin

@admin.register(Reimbursement)
class ReimbursementAdmin(ModelAdmin):
    pass