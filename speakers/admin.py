# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import Speaker, KindContact


class ContactInline(admin.TabularInline):
    """
    Formulario de contatos em linha
    """
    model = KindContact
    extra = 2


class SpeakerAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD do model Speaker
    """

    inlines = [ContactInline, ]

    # campo slug setado como pre-populado de acordo com o que se digita no nome
    prepopulated_fields = {'slug': ('name',)}

    # campos a serem exibidos na tabela
    list_display = (
        'name', 'slug', 'bio',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('name', 'slug', 'created', )

    list_filter = ('created', )

admin.site.register(Speaker, SpeakerAdmin)
