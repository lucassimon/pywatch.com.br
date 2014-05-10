# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import SpeakerUser, KindContact
from .forms import SpeakerUserCreationForm, SpeakerUserChangeForm


class ContactInline(admin.TabularInline):
    """
    Formulario de contatos em linha
    """
    model = KindContact
    extra = 2


class SpeakerUserAdmin(UserAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD do model Speaker
    """
    # formulario para adicionar usuarios palestrantes
    add_form = SpeakerUserCreationForm

    # formulario para alterar usuarios
    form = SpeakerUserChangeForm

    inlines = [ContactInline, ]

    # campos a serem exibidos na tabela
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'slug',
        'bio',
        'created'
    )

    # campos que podem ser filtrados
    list_filter = (
        'created',
        'is_staff',
        'is_superuser',
        'is_active',
        'groups'
    )

    # campos que utilizam buscas no model
    search_fields = (
        'first_name',
        'email',
        'slug',
        'created',
    )

    filter_horizontal = (
        'groups',
        'user_permissions',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password'
                )
            }
        ),
        (
            _(u'Informações pessoais'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'slug',
                    'bio',
                )
            }
        ),
        (
            _(u'Permissões'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _(u'Datas importantes'),
            {
                'fields': (
                    'last_login',
                )
            }
        ),
    )

    ordering = (
        'email',
    )

    date_hierarchy = 'created'


admin.site.register(SpeakerUser, SpeakerUserAdmin)
