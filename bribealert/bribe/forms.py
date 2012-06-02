from django.forms import *
from models import Bribe

class BribeForm(ModelForm):
	class Meta:
		model = Bribe

class NationalChapterForm(Form):
    lat = forms.FloatField()
    lon = forms.FloatField()
