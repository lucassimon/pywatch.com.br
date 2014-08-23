# -*- coding:utf-8 -*-

# Core Django imports
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import formset_factory

# Thirdy Apps imports
from taggit.forms import TagWidget

# Realative imports of the 'app-name' package
from .models import Serie, Screencast, MediaScreencast


class ScreencastForm(forms.ModelForm):
    u"""
    Classe do formulario de palestras
    """

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = Screencast
        u"""
        Define qual Model será utilizado
        """

        exclude = ['speaker', 'slug']
        u"""
        Exclui o atributo speaker/palestrante do formulário
        """

        help_texts = {
            'event': _(
                u'Selecione o evento corresponde,' +
                u' ou realize um cadastro clicando no "+"'
            ),
        }

        widgets = {
            'serie': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um titulo'),
                }
            ),
            'summary': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um breve texto aqui'),
                }
            ),
            'tags': TagWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira os marcadores'),
                }
            ),
        }


class SerieForm(forms.ModelForm):
    u"""
    Classe do formulario de eventos
    """

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = Serie
        u"""
        Define qual Model será utilizado
        """

        exclude = ['slug']
        u"""
        Exclui o atributo speaker/palestrante do formulário
        """
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um nome'),
                }
            ),
        }


class MediaScreencastForm(forms.ModelForm):
    u"""
    Classe do formulario de medias
    """

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = MediaScreencast
        u"""
        Define qual Model será utilizado
        """

        exclude = ['screencast']
        u"""
        Exclui o atributo speaker/palestrante do formulário
        """

        help_texts = {
            'type': _(
                _(u'Escolha uma das opções')
            ),
        }

        widgets = {
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um titulo'),
                }
            ),
            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira a url aqui'),
                }
            ),
        }


class MediaScreencastCreateAndUpdateForm(forms.ModelForm):
    u"""
    Classe do formulario de medias
    """

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = MediaScreencast
        u"""
        Define qual Model será utilizado
        """

        help_texts = {
            'type': _(
                _(u'Escolha uma das opções')
            ),
        }

        widgets = {
            'screencast': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um titulo'),
                }
            ),
            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira a url aqui'),
                }
            ),
        }


MediaScreencastFormSet = formset_factory(
    MediaScreencastForm,
    extra=2,
    can_delete=True,
    can_order=True,
)
