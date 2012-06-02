from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from bribe.models import Bribe

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^upload/$',   'bribe.views.upload'),
	url(r'^$',          direct_to_template, {'template': 'home.html', 'extra_context': { 
      'bribes': Bribe.objects.published(), 
    }}),
    url(r'^admin/',     include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'bribealert.views.home', name='home'),
    # url(r'^bribealert/', include('bribealert.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
