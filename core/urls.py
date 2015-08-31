# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import (
    IndexHomePageTemplateView,
    CustomRegisterCreateView
)

urlpatterns = patterns(
    'core.views',
    url(
        r'^$',
        IndexHomePageTemplateView.as_view(),
        name='home-page'
    ),
    url(
        r"signup/$",
        CustomRegisterCreateView.as_view(),
        name="core-signup"
    ),
)
