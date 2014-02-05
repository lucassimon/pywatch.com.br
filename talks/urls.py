#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import TalkListView

urlpatterns = patterns(
    'talks.views',
    url(
        r'^$',
        TalkListView.as_view(),
        name='talk-list-view'
    )
)
