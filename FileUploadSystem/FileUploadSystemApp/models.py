from django.db import models

# Create your models here.

class file_upload(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file_name