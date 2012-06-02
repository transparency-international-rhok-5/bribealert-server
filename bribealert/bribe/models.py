from django.db import models

class Bribe(models.Model):
	lon = models.FloatField()
	lat = models.FloatField()
	date = models.DateTimeField()
	secure_token = models.CharField(max_length=32, unique=True)
	record = models.FileField(upload_to='records/')