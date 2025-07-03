from django.contrib import admin
from app.models import Leaves
from unfold.admin import ModelAdmin

@admin.register(Leaves)
class LeavesAdmin(ModelAdmin):
    pass
