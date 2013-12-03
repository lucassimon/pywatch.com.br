# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel


class Speaker(TimeStampedModel):
    """
    Classe model para criar um objeto model
    de palestrante.
    """

    name = models.CharField(
        verbose_name=_(u'Nome'),
        max_length=255
    )

    slug = models.SlugField(
        _(u'Slug'),
        unique=True
    )

    bio = models.TextField(
        _(u'Biográfia'),
    )

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Palestrante')
        verbose_name_plural = _(u'Palestrantes')

    def __unicode__(self):
        return u'%s' % (self.name)


class KindContact(models.Model):
    """Classe para o contato"""
    KINDS = (
        ('PH', _('Telefone')),
        ('E', _('E-mail')),
        ('FX', _('Fax')),
        ('FB', _('Facebook')),
        ('TT', _('Twitter')),
        ('GH', _('Github')),
    )
    speaker = models.ForeignKey(
        'Speaker',
        verbose_name=_('Palestrante')
    )

    kind = models.CharField(
        _(u'Tipo'),
        max_length=2,
        choices=KINDS
    )

    value = models.CharField(
        _(u'Valor'),
        max_length=255
    )

    class Meta:
        verbose_name = _(u'Contato')

    def __unicode__(self):
        return u'%s, %s' % (self.kind, self.value)
