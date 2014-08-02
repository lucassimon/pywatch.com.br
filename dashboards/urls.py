# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.conf.urls import patterns, url
# Third-party app imports

# Imports from your apps
from .views import (
    DashboardIndexTemplateView,
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

from .media_talks_views import (
    MediaTalkCreateView,
    MediaTalkUpdateView,
    MediaTalkListView,
    MediaTalkDeleteView,
)

from .screencasts_views import (
    ScreencastIndexTemplateView,
    ScreencastCreateView,
    ScreencastUpdateView,
    ScreencastListView,
    ScreencastDeleteView,
)

from .serie_views import (
    SerieCreateView,
    SerieUpdateView,
    SerieListView,
    SerieDeleteView,
)

from .media_screencasts_views import (
    MediaScreencastCreateView,
    MediaScreencastUpdateView,
    MediaScreencastListView,
    MediaScreencastDeleteView,
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
        r'^mediatalks/create/(?P<talk_pk>\d+)/$',
        MediaTalkCreateView.as_view(),
        name='dashboard-mediatalk-create-view'
    ),
    url(
        r'^mediatalks/update/(?P<talk_pk>\d+)/(?P<pk>\d+)/$',
        MediaTalkUpdateView.as_view(),
        name='dashboard-mediatalk-update-view'
    ),
    url(
        r'^mediatalks/list/(?P<talk_pk>\d+)/$',
        MediaTalkListView.as_view(),
        name='dashboard-mediatalk-list-view'
    ),
    url(
        r'^mediatalks/delete/(?P<talk_pk>\d+)/(?P<pk>\d+)/$',
        MediaTalkDeleteView.as_view(),
        name='dashboard-mediatalk-delete-view'
    ),
    url(
        r'^screencasts/$',
        ScreencastIndexTemplateView.as_view(),
        name='dashboard-screencast-index-view'
    ),
    url(
        r'^screencasts/create/$',
        ScreencastCreateView.as_view(),
        name='dashboard-screencast-create-view'
    ),
    url(
        r'^screencasts/update/(?P<pk>\d+)$',
        ScreencastUpdateView.as_view(),
        name='dashboard-screencast-update-view'
    ),
    url(
        r'^screencasts/list/$',
        ScreencastListView.as_view(),
        name='dashboard-screencast-list-view'
    ),
    url(
        r'^screencasts/delete/(?P<pk>\d+)$',
        ScreencastDeleteView.as_view(),
        name='dashboard-screencast-delete-view'
    ),
    url(
        r'^series/create/$',
        SerieCreateView.as_view(),
        name='dashboard-serie-create-view'
    ),
    url(
        r'^series/update/(?P<pk>\d+)$',
        SerieUpdateView.as_view(),
        name='dashboard-serie-update-view'
    ),
    url(
        r'^series/list/$',
        SerieListView.as_view(),
        name='dashboard-serie-list-view'
    ),
    url(
        r'^series/delete/(?P<pk>\d+)$',
        SerieDeleteView.as_view(),
        name='dashboard-serie-delete-view'
    ),
    url(
        r'^mediascreencasts/create/(?P<screencast_pk>\d+)/$',
        MediaScreencastCreateView.as_view(),
        name='dashboard-mediascreencast-create-view'
    ),
    url(
        r'^mediascreencasts/update/(?P<screencast_pk>\d+)/(?P<pk>\d+)/$',
        MediaScreencastUpdateView.as_view(),
        name='dashboard-mediascreencast-update-view'
    ),
    url(
        r'^mediascreencasts/list/(?P<screencast_pk>\d+)/$',
        MediaScreencastListView.as_view(),
        name='dashboard-mediascreencast-list-view'
    ),
    url(
        r'^mediascreencasts/delete/(?P<screencast_pk>\d+)/(?P<pk>\d+)/$',
        MediaScreencastDeleteView.as_view(),
        name='dashboard-mediascreencast-delete-view'
    ),
)
