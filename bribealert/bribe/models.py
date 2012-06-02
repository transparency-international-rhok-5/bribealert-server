import string
import random

from django.db import models
from django.conf import settings

class Bribe(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    date = models.DateTimeField()
    secure_token = models.CharField(max_length=32, unique=True, blank=True)
    record = models.FileField(upload_to='records/')
    published = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):        
        self.secure_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(settings.SECURE_TOKEN_LENGTH))

        super(Bribe, self).save(*args, **kwargs)

class Country(models.Model):
    name = models.CharField(max_length=100)
