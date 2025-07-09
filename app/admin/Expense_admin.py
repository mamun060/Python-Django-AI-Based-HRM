from django.contrib import admin
from app.models import Expense
from unfold.admin import ModelAdmin

@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
<<<<<<< HEAD
    pass
=======
    list_display = ("travel_request", "category", "amount", "verified")
    search_fields = ("travel_request__employee__username", "category")
    list_filter = ("verified", "category")
>>>>>>> 34accc8f6043820424f9169cdc62545edc287931
