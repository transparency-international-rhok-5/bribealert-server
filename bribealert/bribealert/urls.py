from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^upload/$', 'bribe.views.upload'),
    url(r'^get_national_chapter/$', 'bribe.views.get_national_chapter'),
    url(r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'bribealert.views.home', name='home'),
    # url(r'^bribealert/', include('bribealert.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
