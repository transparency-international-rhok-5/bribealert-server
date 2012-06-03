import simplejson

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from models import Bribe, NationalChapter, Message
from forms import BribeForm, NationalChapterForm, MessageForm
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

        response = simplejson.dumps(chapter.to_dict())

        return HttpResponse(response, mimetype='application/json')

    return HttpResponseBadRequest()
    
def chat(request, id):
    bribe = get_object_or_404(Bribe, id=id)
    
    form = MessageForm(request.POST or None)

    if form.is_valid():
        new_message = form.save(commit=False)
        new_message.bribe = bribe
        new_message.user = request.user
        new_message.save()
        
        form = MessageForm()
            
    return render_to_response('admin/chat.html', RequestContext(request, {'bribe': bribe, 'form': form}))

def messages(request):
    bribe = Bribe.objects.get(secure_token=request.GET['secure_token'])
    
    response = simplejson.dumps({'messages' : [message.to_dict() for message in bribe.message_set.all()] })
    return HttpResponse(response, mimetype='application/json')
    
def add_message(request):
    bribe = Bribe.objects.get(secure_token=request.GET['secure_token'])
  
    form = MessageForm(request.POST or None)

    if form.is_valid():
        new_message = form.save(commit=False)
        new_message.bribe = bribe
        new_message.save()
        
        form = MessageForm()      
        return HttpResponse(simplejson.dumps({'status' : 'ok' }), mimetype='application/json')
    else:
        return HttpResponseBadRequest()