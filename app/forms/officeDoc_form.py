from django import forms
from app.models import OfficialDocument

class OfficialDocumentForm(forms.ModelForm):
    class Meta:
        model = OfficialDocument
        fields = ['filename' , 'filedescription' , 'file']