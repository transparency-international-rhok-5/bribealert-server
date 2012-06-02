from django.db import models

class Bribe(models.Model):
	lon = models.FloatField()
	lat = models.FloatField()
	date = models.DateTimeField()
	record = models.FileField(upload_to='records/')