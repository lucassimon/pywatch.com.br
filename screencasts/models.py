# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

# Thirdy Apps imports

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel, StandardItemStuffModel,\
    Media
from .managers import ScreencastManager


class Serie(TimeStampedModel):
    """
    Model reponsável por cadastrar as series
    e podem conter vários screencasts.
    """

    name = models.CharField(
        verbose_name=_(u'Nome'),
        max_length=255
    )
    """
    Atributo da classe  para identificar um evento
    e seu nome

    Caracteristicas:
    CharField
    verbose name: Nome
    max length: 255
    """

    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        max_length=255,
        unique=True,
        null=True
    )
    """
    Atributo da classe para criar um slug baseado
    no nome do evento

    Caracteristicas:
    SlugField
    verbose name: Slug
    max length: 255
    """

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Serie')
        verbose_name_plural = _(u'Series')

    def __unicode__(self):
        return u'%s' % (self.name)


class Screencast(TimeStampedModel, StandardItemStuffModel):
    """
    Model responsavel pelos screencasts gravados
    pela comunidade
    """

    serie = models.ForeignKey(
        Serie,
        verbose_name=_(u'Serie'),
        blank=True,
        null=True
    )
    """
    Atributo da classe Talk para
    referenciar um objeto da classe Event

    Caracteristicas:
    ForeignKey
    verbose name: Evento
    """

    objects = ScreencastManager()

    def get_absolute_url(self):
        """
        Retorna o caminho absoluto da instancia
        do objeto, através do reverse
        usando namespace definido no arquivo
        urls.py
        """
        return reverse('screencasts:screencast-detail-view', args=[self.slug])

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Screencasts')
        verbose_name_plural = _(u'Screencasts')

    def __unicode__(self):
        return u'%s' % (self.title)


class MediaScreencast(Media):
    """
    Model responsavel por criar as medias
    dos screencasts
    """

    screencast = models.ForeignKey(
        'Screencast',
        verbose_name=_(u'Screencasts'),
        related_name='medias'
    )

    """
    Atributo da classe MediaScreencast para referenciar
    ao objeto da classe Screencast
    """

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Media dos screencasts')
        verbose_name_plural = _(u'Medias dos screencasts')

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.url)
