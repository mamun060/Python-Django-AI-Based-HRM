from django.contrib import admin
from app.models import TravelRequest
from unfold.admin import ModelAdmin

@admin.register(TravelRequest)
class TravelRequestAdmin(ModelAdmin):
    pass