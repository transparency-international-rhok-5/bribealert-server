import string
import random

from pygeocoder import Geocoder

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.forms.models import model_to_dict

import twitter

class BribeManager(models.Manager):
    def published(self):
        return self.filter(published=True).order_by('-date')
    
class Bribe(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    country = models.ForeignKey('Country', blank=True, null=True)
    date = models.DateTimeField()
    secure_token = models.CharField(max_length=32, unique=True, blank=True)
    record = models.FileField(upload_to='records/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    
    objects = BribeManager()
    
    def chat_link(self): 
        from django.utils.safestring import mark_safe 
        return mark_safe('<a href="/admin/chat/%d/">Contact whistleblower</a>' % (self.id, )) 

    chat_link.short_description = "Chat" 
    chat_link.allow_tags = True
    
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
        if self.published:
            api = twitter.Api(consumer_key='0A8C16ZwuUKj93gDUbIcZw',
            consumer_secret='jZ44hJjGfYAeyvkNoJn2YVzeToE7vgcVeelUF2A814',
            access_token_key='598222089-ZVMJ1BnrBccjTdqh3DojaPJPvc7ScgBDX8mCljeh',
            access_token_secret='rth7eys2w6KCAisslsep1KDzFTczuoFVhOknpl5m20s')
            status = api.PostUpdate('A new bribe was reported! www.bribe-alert.org/#bribe%d' % (self.id))
            print 'tweet sent, "%s"' % (status)

    def __unicode__(self):
        return unicode(Geocoder.reverse_geocode(self.lat, self.lon)[0])

class Country(models.Model):
    name = models.CharField(max_length=100)
    code2 = models.CharField(max_length=2, unique=True)
    code3 = models.CharField(max_length=3, unique=True)
    
    def __unicode__(self):
        return self.name

class NationalChapter(Group):
    country = models.ForeignKey('Country')
    street = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)
    
    def to_dict(self):
        result = model_to_dict(self, fields= ['street', 'zipcode', 'city', 'telephone', 'fax', 'email', 'url'])
        result['country'] = self.country.name
        
        return result
        
class Message(models.Model):
    # in case there is no user from a national chapter that is assigned to an instance
    # the message was sent by the whistle blower
    user = models.ForeignKey(User, null=True)
    bribe = models.ForeignKey(Bribe)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    def to_dict(self):
        result = model_to_dict(self, fields= ['text'])
        result['date'] = str(self.date)

        if self.user:
            result['user'] = self.user.__unicode__()
        
        return result
