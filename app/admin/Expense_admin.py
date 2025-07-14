from django.contrib import admin
from app.models import Expense
from unfold.admin import ModelAdmin

@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    pass
    list_display = ("name", "expense_type", "amount", "verified", "receipt")
    search_fields = ("name", "expense_type")
    list_filter = ("verified", "expense_type")
    ordering = ('-id',)
    list_per_page = 20