from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class Profile(models.Model):
    BAND = (('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'),('E', 'E'),('F', 'F'))

    user = models.OneToOneField(User, related_name="profile")
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = CountryField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    discount = models.CharField(max_length=10, choices=BAND, default='A', null=True)
    vat = models.BooleanField(default=False)
    mailing_list = models.BooleanField(default=True)
    special_offers = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


def create_profil_user_callback(sender, instance, **kwargs):
    profil, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_profil_user_callback, User)
