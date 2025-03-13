from django.contrib import admin 
from app.models import Documents

class OfficialDocumentAdmin(admin.ModelAdmin):
    list_display = ('filename' , 'filedescription' , 'file')
    search_fields = ('filename', )
admin.site.register(Documents, OfficialDocumentAdmin)