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

class Session(models.Model):
    session_key = models.CharField(max_length=255, null=True, blank=True, editable=False)
    user = models.ForeignKey(User, related_name="user_visit", editable=False)
    ipaddress = models.CharField(max_length=40, null=True, blank=True, editable=False)
    time_on_site = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Session"

    def __unicode__(self):
        return self.session_key
