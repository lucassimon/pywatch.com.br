# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Realative imports of the 'app-name' package


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified``
    fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StandardItemStuffModel(models.Model):
    """
    Classe abstrata para comportar campos em comum
    com os as apps de palestras/talks,
    screencasts, tutoriais/artigos,
    """

    speaker = models.ForeignKey(
        'speakers.Speaker',
        verbose_name=_(u'Palestrante'),
    )

    title = models.CharField(
        verbose_name=_(u'Titulo'),
        max_length=255
    )

    summary = models.TextField(
        verbose_name=_(u'Sumário')
    )

    class Meta:
        abstract = True


class Media(TimeStampedModel):
    """
    Classe model para cadastrar as medias
    com os as apps de palestras/talks,
    screencasts, tutoriais/artigos,
    """

    _KIND_MEDIAS = (
        ('TU', _(u'Tutorial')),
        ('CD', _(u'Codigo')),
        ('VI', _(u'Video')),
        ('SL', _(u'Slide')),
    )

    type = models.CharField(
        verbose_name=_(u'Tipo'),
        max_length=3,
        choices=_KIND_MEDIAS
    )

    title = models.CharField(
        verbose_name=_(u'Titulo'),
        max_length=255
    )

    url = models.URLField(
        verbose_name=_('URL'),
    )

    class Meta:
        abstract = True
