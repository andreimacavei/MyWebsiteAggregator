from django.conf.urls import patterns, include, url
from mywebsite.views import *

from reader.views import homepage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywebsite.views.home', name='home'),
    # url(r'^mywebsite/', include('mywebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Urls created by me
    url(r'time/$', current_date),
    url(r'time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^polls/$', index),
    # Urls for reader app
    url(r'^$', homepage),
)
