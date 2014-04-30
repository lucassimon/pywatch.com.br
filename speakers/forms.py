
# -*- coding:utf-8 -*-

# Core Django imports
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Realative imports of the 'app-name' package
from .models import SpeakerUser


class SpeakerUserCreationForm(forms.ModelForm):
    """
    Um formulário para criar novos usuários. Incluindo
    todos os campos requeridos
    """
