from django import forms
from models import Bribe

class BribeForm(forms.ModelForm):
	class Meta:
		model = Bribe

class NationalChapterForm(forms.Form):
    lat = forms.FloatField()
    lon = forms.FloatField()
