from django import forms
from app.models import Documents

class OfficialDocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['filename' , 'filedescription' , 'file']