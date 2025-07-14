from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.rar']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class Document(models.Model):
    filename = models.CharField(max_length=255)
    filedescription = models.TextField()
    file = models.FileField(upload_to='officialDocs/', validators=[validate_file_extension])

    def __str__(self):
        return self.filename