from django import forms
from models import Bribe, Message

class BribeForm(forms.ModelForm):
    class Meta:
        model = Bribe
		
class MessageForm(forms.ModelForm):
    class Meta:
        fields = ('text',)
        model = Message

class NationalChapterForm(forms.Form):
    lat = forms.FloatField()
    lon = forms.FloatField()
