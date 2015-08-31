#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include

from .views import ScreencastListView, ScreencastDetailView

urlpatterns = patterns(
    'screencasts.views',
    url(
        r'^$',
        ScreencastListView.as_view(),
        name='screencast-list-view'
    ),
    url(
        r'^(?P<slug>[-_\w]+)/$',
        ScreencastDetailView.as_view(),
        name='screencast-detail-view'
    )
)
