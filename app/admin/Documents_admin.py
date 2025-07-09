from django.contrib import admin 
from app.models import Document
from unfold.admin import ModelAdmin
<<<<<<< HEAD
=======
from django.utils.html import format_html
>>>>>>> 34accc8f6043820424f9169cdc62545edc287931

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
<<<<<<< HEAD
# admin.site.register(Document, DocumentsAdmin)
=======
# admin.site.register(Document, DocumentsAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'pdf_link')

    def pdf_link(self, obj):
        file_name = obj.generated_pdf_name  # Example: Invoice_-_SERINV00000005.pdf
        url = f"/officialDocs/{file_name}"
        return format_html('<a href="{}" target="_blank">View Invoice</a>', url)

    pdf_link.short_description = "Invoice PDF"
>>>>>>> 34accc8f6043820424f9169cdc62545edc287931
