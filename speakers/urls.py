# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import (
    SpeakerListView,
    SpeakerDetailView,
    SpeakerProfileTemplateView,
    SpeakerBasicInformationProfile,
    KindContactCreateView,
    KindContactUpdateView,
    KindContactDeleteView,
)

urlpatterns = patterns(
    'speakers.views',
    url(
        r'^$',
        SpeakerListView.as_view(),
        name='speaker-list-view'
    ),
    url(
        r'^profile/$',
        SpeakerProfileTemplateView.as_view(),
        name='speaker-profile-view'
    ),
    url(
        r'^profile/basic-information$',
        SpeakerBasicInformationProfile.as_view(),
        name='speaker-profile-save-basic-information'
    ),
    url(
        r'^profile/contacts/create/$',
        KindContactCreateView.as_view(),
        name='speaker-profile-contact-create-view'
    ),
    url(
        r'^profile/contacts/update/(?P<pk>\d+)$',
        KindContactUpdateView.as_view(),
        name='speaker-profile-contact-update-view'
    ),
    url(
        r'^profile/contacts/delete/(?P<pk>\d+)$',
        KindContactDeleteView.as_view(),
        name='speaker-profile-contact-delete-view'
    ),
    url(
        r'^(?P<slug>[-_\w]+)/$',
        SpeakerDetailView.as_view(),
        name='speaker-detail-view'
    )
)
