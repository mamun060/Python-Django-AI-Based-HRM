from django.contrib import admin
from app.models import Expense
from unfold.admin import ModelAdmin

@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    pass