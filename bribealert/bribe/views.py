import simplejson

from django.http import HttpResponseBadRequest
from forms import BribeForm

def upload(request):
	form = BribeForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		new_bribe = form.save()
		response = simplejson.dumps({'id': new_bribe.id})
		
		return HttpResponseRedirect(response, mimetype='application/json')

	return HttpResponseBadRequest()