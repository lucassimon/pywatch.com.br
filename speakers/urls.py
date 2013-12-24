#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import SpeakerListView

urlpatterns = patterns(
    'speakers.views',
    url(
        r'^$',
        SpeakerListView.as_view(),
        name='speaker-list-view'
    )
)
