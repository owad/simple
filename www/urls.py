# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from www import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = None

if settings.DEBUG:
    urlpatterns = patterns('django.views.static',
    (r'^static/(?P<path>.*)$',
        'serve', {
        'document_root': '/home/owad/workspace/lule/www/static',
        'show_indexes': True }),)


urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('www.page.urls')),
)
