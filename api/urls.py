#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from speakers.views import SpeakerList, SpeakerDetail

urlpatterns = patterns(
    'api.views',
    url(
        r'^speakers/$',
        SpeakerList.as_view(),
        name='speaker-list'
    ),
    url(
        r'^speakers/(?P<pk>\d+)/$',
        SpeakerDetail.as_view(),
        name='speaker-detail'
    )
)
