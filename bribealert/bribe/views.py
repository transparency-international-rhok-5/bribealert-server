import simplejson

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Bribe, NationalChapter
from forms import BribeForm, NationalChapterForm
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
    form = NationalChapterForm(request.GET)

    if form.is_valid():
        country = get_country_from_geo_location(float(request.GET['lat']), float(request.GET['lon']))
        chapter = NationalChapter.objects.get(country=country)

        response = simplejson.dumps(chapter.serialize())

        return HttpResponse(response, mimetype='application/json')

    return HttpResponseBadRequest()
