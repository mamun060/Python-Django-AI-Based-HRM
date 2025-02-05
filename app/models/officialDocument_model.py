from django.db import models


class OfficialDocument(models.Model):
    filename = models.CharField(max_length=255)
    filedescription = models.TextField()
    file = models.FileField(upload_to='officialDocs/')

    def __str__(self):
        return self.filename