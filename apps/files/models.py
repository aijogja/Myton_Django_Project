from django.db import models
import uuid
import os

# Create your models here.


class Download(models.Model):

    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('download', filename)

    title = models.CharField(max_length=255, null=True)
    file_upload = models.FileField(
        verbose_name='File', upload_to=get_file_path, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "File Download"

    def __unicode__(self):
        return self.title
