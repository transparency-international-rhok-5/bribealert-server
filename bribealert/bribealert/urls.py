from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bribe.models import Bribe

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^upload/$',   'bribe.views.upload'),
    url(r'^get_national_chapter/$', 'bribe.views.get_national_chapter'),
	url(r'^$',          direct_to_template, {'template': 'home.html', 'extra_context': { 
	    'bribes': Bribe.objects.published(), 
    }}),    
    url(r'^admin/',     include(admin.site.urls)),
)
