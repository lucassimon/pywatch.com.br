# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import Talk, MediaTalk


class MediaInline(admin.TabularInline):
    """
    Formulario de media em linha
    """
    model = MediaTalk
    extra = 2


class TalkAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD do model Talk
    """

    inlines = [MediaInline, ]

    # campo slug setado como pre-populado de acordo com o que se digita no nome
    prepopulated_fields = {'slug': ('title', )}

    # campos a serem exibidos na tabela
    list_display = (
        'speaker', 'title', 'summary',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('title', 'created', )

    list_filter = ('created', )

admin.site.register(Talk, TalkAdmin)
