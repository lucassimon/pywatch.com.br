
# -*- coding:utf-8 -*-

# Core Django imports
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Realative imports of the 'app-name' package
from .models import SpeakerUser


class SpeakerUserCreationForm(UserCreationForm):
    class Meta:
        model = SpeakerUser
        fields = ('username',)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            SpeakerUser._default_manager.get(username=username)
        except SpeakerUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class SpeakerUserChangeForm(UserChangeForm):
        class Meta:
            model = SpeakerUser
