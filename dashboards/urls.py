# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
# Third-party app imports

# Imports from your apps
from .views import (
    DashboardIndexTemplateView,
    ScreencastIndexTemplateView,
)

from .talk_views import (
    TalkIndexTemplateView,
    TalkCreateView,
    TalkUpdateView,
    TalkListView,
    TalkDeleteView,
)

from .event_views import (
    EventCreateView,
    EventUpdateView,
    EventListView,
    EventDeleteView,
)


urlpatterns = patterns(
    'dashboards.views',
    url(
        r'^$',
        DashboardIndexTemplateView.as_view(),
        name='dashboard-index-view'
    ),
    url(
        r'^talks/$',
        TalkIndexTemplateView.as_view(),
        name='dashboard-talk-index-view'
    ),
    url(
        r'^talks/create/$',
        TalkCreateView.as_view(),
        name='dashboard-talk-create-view'
    ),
    url(
        r'^talks/update/(?P<pk>\d+)$',
        TalkUpdateView.as_view(),
        name='dashboard-talk-update-view'
    ),
    url(
        r'^talks/list/$',
        TalkListView.as_view(),
        name='dashboard-talk-list-view'
    ),
    url(
        r'^talks/delete/(?P<pk>\d+)$',
        TalkDeleteView.as_view(),
        name='dashboard-talk-delete-view'
    ),
    url(
        r'^events/create/$',
        EventCreateView.as_view(),
        name='dashboard-event-create-view'
    ),
    url(
        r'^events/update/(?P<pk>\d+)$',
        EventUpdateView.as_view(),
        name='dashboard-event-update-view'
    ),
    url(
        r'^events/list/$',
        EventListView.as_view(),
        name='dashboard-event-list-view'
    ),
    url(
        r'^events/delete/(?P<pk>\d+)$',
        EventDeleteView.as_view(),
        name='dashboard-event-delete-view'
    ),
    url(
        r'^screencasts/$',
        ScreencastIndexTemplateView.as_view(),
        name='dashboard-screencast-index-view'
    ),
)
