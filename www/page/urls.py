# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
from www.page.views import FlatPageView

urlpatterns = patterns('www.page.views',
    url(r'^', FlatPageView.as_view(), name='page'),
)

