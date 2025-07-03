from django.contrib import admin 
from app.models import Document
from unfold.admin import ModelAdmin

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ('filename', 'filedescription', 'file')
    search_fields = ('filename',)
    list_filter = ('filedescription',)
    ordering = ('-id',)
    list_per_page = 20
# class DocumentsAdmin(admin.ModelAdmin):
#     list_display = ('filename' , 'filedescription' , 'file')
#     search_fields = ('filename', )
# admin.site.register(Document, DocumentsAdmin)