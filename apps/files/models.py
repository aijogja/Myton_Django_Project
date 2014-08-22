from django.db import models
from datetime import datetime
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
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

class ProductList(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('product', filename)

    title = models.CharField(max_length=255, null=True, editable=False)
    file_upload = models.FileField(
        verbose_name='File', upload_to=get_file_path, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super(ProductList, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     storage, path = self.file_upload.storage, self.file_upload.path
    #     super(ProductList, self).delete(*args, **kwargs)
    #     storage.delete(path)

    class Meta:
        verbose_name_plural = "Product List Upload"

    def __unicode__(self):
        return self.title

@receiver(pre_delete, sender=ProductList)
def file_upload_delete(sender, instance, **kwargs):
        if instance.file_upload :
                instance.file_upload.delete(False)

