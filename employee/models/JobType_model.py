from django.db import models

class JobType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Job Types"
        ordering = ['name']
