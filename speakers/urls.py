# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import (
    SpeakerListView,
    SpeakerDetailView,
    SpeakerProfileTemplateView,
    save_basic_information_profile,
    # save_speaker_contacts_information_profile,
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
        save_basic_information_profile,
        name='speaker-profile-save-basic-information'
    ),
    # url(
    #     r'^profile/contacts$',
    #     save_speaker_contacts_information_profile,
    #     name='speaker-profile-save-contacts-information'
    # ),
    url(
        r'^(?P<slug>[-_\w]+)/$',
        SpeakerDetailView.as_view(),
        name='speaker-detail-view'
    )
)
