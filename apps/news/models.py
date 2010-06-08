from django.db import models

from timezones.fields import TimeZoneField
from perms.models import AuditingBaseModel
from news.managers import NewsManager

class News(AuditingBaseModel):
    guid = models.CharField(max_length=50, unique=False, blank=True)
    timezone = TimeZoneField()
    headline = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    source = models.CharField(max_length=300, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=300, blank=True)
    release_dt = models.DateTimeField(null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    syndicate = models.BooleanField()
    design_notes = models.TextField(blank=True)

    # TODO: wonder if type and length are missing
    enclosure_url = models.CharField(max_length=500, blank=True)
    useautotimestamp = models.BooleanField()
    
    objects = NewsManager()

    class Meta:
        permissions = (("view_news","Can view news"),)
        verbose_name_plural = "news"

    def get_absolute_url(self):
        return ('news.view', [self.pk])
    get_absolute_url = models.permalink(get_absolute_url)
      
    def __unicode__(self):
        return self.headline