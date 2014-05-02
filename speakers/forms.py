
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
    first_name = forms.CharField(
        label=_(u'Primeiro Nome'),
        max_length=100,
    )
    """
    Atributo do formulário para setar o primeiro nome
    """

    last_name = forms.CharField(
        label=_(u'Último Nome'),
        max_length=100,
    )
    """
    Atributo do formulário para setar o ultimo nome
    """

    password = forms.CharField(
        label=_(u'Senha'),
        widget=forms.PasswordInput
    )
    """
    Atributo do formulário para setar uma senha
    """

    repeat_password = forms.CharField(
        label=_(u'Confirme a senha'),
        widget=forms.PasswordInput
    )
    """
    Atributo do formulário para repetir a senha
    digitada no campo password
    """

    class Meta:
        model = SpeakerUser
        fields = ('email',)

    def clean_repeat_password(self):
        """
        Verifica se as duas senhas digitadas conferem
        """
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError(
                _(u'As senhas não conferem')
            )
        return repeat_password

    def save(self):
        """
        Salva a senha fornecida
        """
        user = super(
            SpeakerUserCreationForm,
            self
        ).save(
            commit=False
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SpeakerUserChangeForm(forms.ModelForm):
    """
    Um form para atualizar os usuários, incluindo todos os campos
    do usuário, mas alterando o campo senha para um campo de somente
    leitura
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SpeakerUser

    def clean_password(self):
        """

        """
        return self.initial['password']
