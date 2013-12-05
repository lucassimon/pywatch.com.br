# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel, StandardItemStuffModel,\
    Media


class Talk(TimeStampedModel, StandardItemStuffModel):
    """
    Model responsavel pelos palestrante
    """

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Palestras')
        verbose_name_plural = _(u'Palestras')

    def __unicode__(self):
        return u'%s' % (self.name)


class MediaTalk(Media):
    """
    Model responsavel por criar as medias
    de palestrantes
    """

    talk = models.ForeignKey(
        'Talk',
        verbose_name=_(u'Palestras')
    )

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Media Palestrante')
        verbose_name_plural = _(u'Medias Palestrantes')

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.url)
