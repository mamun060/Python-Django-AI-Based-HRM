from django.contrib import admin 
from app.models import Document

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('filename' , 'filedescription' , 'file')
    search_fields = ('filename', )
admin.site.register(Document, DocumentsAdmin)