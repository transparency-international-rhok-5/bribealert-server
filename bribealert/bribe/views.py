import simplejson

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Bribe
from forms import BribeForm
from helpers import get_country_from_geo_location

@csrf_exempt
def upload(request):
    form = BribeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        new_bribe = form.save()
        response = simplejson.dumps({'id': new_bribe.id})

        return HttpResponse(response, mimetype='application/json')

    return HttpResponseBadRequest()


def get_national_chapter(request):
    pass
