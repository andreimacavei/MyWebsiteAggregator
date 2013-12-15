from django.conf.urls import patterns, url
from reader import views

urlpatterns = patterns('',
    url(r'^$', views.get_feeds, name='get_feeds'),
)