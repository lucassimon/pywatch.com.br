# -*- coding:utf-8 -*-

# Core Django imports
from django import forms
from django.utils.translation import ugettext_lazy as _

# Thirdy Apps imports

# Realative imports of the 'app-name' package
from .models import Event, Talk, MediaTalk


class TalkForm(forms.ModelForm):
    u"""
    Classe do formulario de palestras
    """

    class Meta:
        u"""
        Define atributos do formulario
        """

        model = Talk
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
            'event': forms.Select(
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
            'tags': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira os marcadores'),
                }
            ),
        }
