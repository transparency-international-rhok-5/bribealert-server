from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bribe.models import Bribe

admin.autodiscover()

urlpatterns = patterns('',
	(r'^upload/$',                      'bribe.views.upload'),
    (r'^messages/$',                	'bribe.views.messages'),
    (r'^messages/add/$',            	'bribe.views.add_message'),
    (r'^admin/chat/(?P<id>\d+)/$',	    'bribe.views.chat'),
    (r'^national-chapter/$',            'bribe.views.get_national_chapter'),
	(r'^$',                             'bribe.views.home'),    
    (r'^admin/',                        include(admin.site.urls)),
    (r'^media/(?P<path>.*)$',           'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
