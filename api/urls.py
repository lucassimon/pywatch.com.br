#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from speakers.views import SpeakerList, SpeakerDetail
from talks.views import TalkList, TalkDetail
from .views import api_root

urlpatterns = patterns(
    '',
    url(
        r'^$',
        api_root
    ),
    url(
        r'^speakers/$',
        SpeakerList.as_view(),
        name='speaker-list'
    ),
    url(
        r'^speakers/(?P<pk>\d+)/$',
        SpeakerDetail.as_view(),
        name='speaker-detail'
    ),
    url(
        r'^talks/$',
        TalkList.as_view(),
        name='talk-list'
    ),
    url(
        r'^talks/(?P<pk>\d+)/$',
        TalkDetail.as_view(),
        name='talk-detail'
    )
)
