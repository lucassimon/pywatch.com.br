# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
# Third-party app imports

# Imports from your apps
from .views import DashboardIndexTemplateView

urlpatterns = patterns(
    'dashboards.views',
    url(
        r'^$',
        login_required(DashboardIndexTemplateView.as_view()),
        name='dashboard-index-view'
    ),
)
