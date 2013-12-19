#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import IndexHomePageTemplateView

urlpatterns = patterns(
    'core.views',
    url(
        r'^$',
        IndexHomePageTemplateView.as_view()
    )
)
