from django.forms import ModelForm
from models import Bribe

class BribeForm(ModelForm):
	class Meta:
		model = Bribe
