# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin

# Third-party app imports
from mptt.admin import MPTTModelAdmin

# Realative imports of the 'app-name' package
from .models import Screencast, MediaScreencast, Serie


class MediaInline(admin.TabularInline):
    """
    Formulario de media em linha
    """
    model = MediaScreencast
    extra = 2


class ScreencastAdmin(admin.ModelAdmin):
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


class SerieAdmin(MPTTModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD do model Serie
    """
    # campo slug setado como pre-populado de acordo com o que se digita no nome
    prepopulated_fields = {'slug': ('parent', 'name', )}

    # campos a serem exibidos na tabela
    list_display = (
        'name',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('name', 'created', )

    list_filter = ('created', )

admin.site.register(Screencast, ScreencastAdmin)
admin.site.register(Serie, SerieAdmin)
