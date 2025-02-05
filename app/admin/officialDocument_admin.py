from django.contrib import admin 
from app.models import OfficialDocument

class OfficialDocumentAdmin(admin.ModelAdmin):
    list_display = ('filename' , 'filedescription' , 'file')
    search_fields = ('filename', )
admin.site.register(OfficialDocument, OfficialDocumentAdmin)