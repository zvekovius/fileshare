from django.db import models
from django.utils import timezone

# Create your models here.
class Files(models.Model):
    file_name = models.CharField(max_length=200)
    extension = models.CharField(max_length=5)
    uploaded_datetime = models.DateTimeField(default=timezone.now)

    def push(self):
        self.uploaded_datetime = timezone.now()

    def __str__(self):
        return self.file_name
