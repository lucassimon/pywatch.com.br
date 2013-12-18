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
    """
    Atributo da classe Speaker para setar o nome
    do palestrante.

    Caracteristicas:
    max length: 255
    """

    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        unique=True
    )
    """
    Atributo da classe Speaker para setar o slug
    do palestrante.

    Caracteristicas:
    max length: 255
    unique: True
    """

    bio = models.TextField(
        verbose_name=_(u'Biográfia'),
    )
    """
    Atributo da classe Speaker para setar a biografria
    do palestrante.

    Caracteristicas:
    TextField
    """

    class Meta:
        """
        Seta a ordenação da listagem pelo campo `created` ascendente
        Nome da app no singular e plural
        """
        ordering = ['created']
        verbose_name = _(u'Palestrante')
        verbose_name_plural = _(u'Palestrantes')

    def __unicode__(self):
        """
        Retorna o nome do palestrante
        como unicode.
        """
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
        ('GG', _('Google')),
    )

    speaker = models.ForeignKey(
        'Speaker',
        verbose_name=_('Palestrante')
    )

    """
    Atributo da classe KindContact para referenciar
    ao objeto da classe speaker
    """

    kind = models.CharField(
        _(u'Tipo'),
        max_length=2,
        choices=KINDS
    )
    """
    Atributo da classe KindContact para escolher as
    opcoes setada na tupla KINDS

    Caracteristicas:
    CharField
    max length: 2
    """

    value = models.CharField(
        _(u'Valor'),
        max_length=255
    )
    """
    Atributo da classe KindContact para setar o
    valor da opção escolhida

    Caracteristicas:
    CharField
    max length: 255
    """

    class Meta:
        """
        """
        verbose_name = _(u'Contato')

    def __unicode__(self):
        """
        Retorna o tipo e valor
        como unicode.
        """
        return u'%s, %s' % (self.kind, self.value)
