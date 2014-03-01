#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import SpeakerListView, SpeakerDetailView

urlpatterns = patterns(
    'speakers.views',
    url(
        r'^$',
        SpeakerListView.as_view(),
        name='speaker-list-view'
    ),
    url(
        r'^(?P<slug>[-_\w]+)/$',
        SpeakerDetailView.as_view(),
        name='speaker-detail-view'
    )
)
