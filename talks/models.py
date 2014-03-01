# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel, StandardItemStuffModel,\
    Media
from .managers import TalkMostRecentCreatedManager


class Talk(TimeStampedModel, StandardItemStuffModel):
    """
    Model responsavel pelos palestrante
    """

    objects = TalkMostRecentCreatedManager()

    def get_absolute_url(self):
        """
        Retorna o caminho absoluto da instancia
        do objeto, através do reverse
        usando namespace definido no arquivo
        urls.py
        """
        return reverse('talks:talk-detail-view', args=[self.slug])

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Palestras')
        verbose_name_plural = _(u'Palestras')

    def __unicode__(self):
        return u'%s' % (self.title)


class MediaTalk(Media):
    """
    Model responsavel por criar as medias
    de palestrantes
    """

    talk = models.ForeignKey(
        'Talk',
        verbose_name=_(u'Palestras'),
        related_name='medias'
    )

    """
    Atributo da classe MediaTalk para referenciar
    ao objeto da classe Talk
    """

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Media Palestrante')
        verbose_name_plural = _(u'Medias Palestrantes')

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.url)
