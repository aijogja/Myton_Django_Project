from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Search(models.Model):
    keyword = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, related_name="search")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Search"

    def __unicode__(self):
        return self.keyword
