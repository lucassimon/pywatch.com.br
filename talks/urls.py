#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import TalkListView, TalkDetailView

urlpatterns = patterns(
    'talks.views',
    url(
        r'^$',
        TalkListView.as_view(),
        name='talk-list-view'
    ),
    url(
        r'^(?P<slug>[-_\w]+)/$',
        TalkDetailView.as_view(),
        name='talk-detail-view'
    )
)
