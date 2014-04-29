# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel, StandardItemStuffModel,\
    Media


class Screencast(TimeStampedModel, StandardItemStuffModel):
    """
    Model responsavel pelos screencasts gravados
    pela comunidade
    """

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
