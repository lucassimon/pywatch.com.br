
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


class SpeakerBasicInformationForm(forms.ModelForm):
    u"""
    Classe para o formulário de edição básica das
    informações do palestrante
    """
    def __init__(self, *args, **kwargs):
        super(SpeakerBasicInformationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = SpeakerUser
        u"""
        Define qual Model será utilizado
        """

        fields = ('first_name', 'last_name', 'bio',)
        u"""
        Atributos que irão aparecer no formulário
        """

        help_texts = {
            'first_name': _(
                u'Exemplo: Jhon'
            ),
            'last_name': _(
                u'Exemplo: Doe'
            ),
            'bio': _(
                u'Jhon Doe é programador django/python'
            ),
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira o primeiro nome'),
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira o último nome'),
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um breve texto aqui'),
                }
            ),
        }
