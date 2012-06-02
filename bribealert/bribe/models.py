import string
import random

from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

class Bribe(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    country = models.ForeignKey('Country', blank=True, null=True)
    date = models.DateTimeField()
    secure_token = models.CharField(max_length=32, unique=True, blank=True)
    record = models.FileField(upload_to='records/')
    published = models.BooleanField(default=False)
    
    def __generate_secure_token(self):
        while 1:
            secure_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(settings.SECURE_TOKEN_LENGTH))
            try:
			    self.__class__.objects.get(secure_token=secure_token)
            except self.__class__.DoesNotExist:
                return secure_token
    
    def save(self, *args, **kwargs):
        from bribe.helpers import get_country_from_geo_location
        
        self.secure_token = self.__generate_secure_token()
        self.country = get_country_from_geo_location(self.lat, self.lon)
        super(Bribe, self).save(*args, **kwargs)

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class NationalChapter(Group):
    country = models.ForeignKey('Country')