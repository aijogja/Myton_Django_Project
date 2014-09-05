from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, null=True, editable=False)
    content = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='article', null=True)
    image_thumb = ImageSpecField(
        source='image', processors=[ResizeToFill(200, 100)],
        format='JPEG', options={'quality': 60})
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title