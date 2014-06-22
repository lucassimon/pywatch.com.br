# -*- coding:utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

urlpatterns = patterns(
    'dashboards.views',
    url(
        r'^$',
        login_required(DashboardIndexTemplateView.as_view()),
        name='dashboard-index-view'
    ),
)
