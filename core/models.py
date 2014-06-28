# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Realative imports of the 'app-name' package
from taggit.managers import TaggableManager


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified``
    fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    """
    Atributo da classe TimeStampedModel para
    referenciar um campo de data de criação

    Caracteristicas:
    DateTimeField
    auto now add: True
    """

    modified = models.DateTimeField(auto_now=True)
    """
    Atributo da classe TimeStampedModel para
    referenciar um campo de data de modificado

    Caracteristicas:
    DateTimeField
    auto now: True
    """

    class Meta:
        """
        Seta a classe como abstrata
        """
        abstract = True


class StandardItemStuffModel(models.Model):
    """
    Classe abstrata para comportar campos em comum
    com os as apps de palestras/talks,
    screencasts, tutoriais/artigos,
    """

    speaker = models.ForeignKey(
        'speakers.SpeakerUser',
        verbose_name=_(u'Palestrante'),
        help_text=_(u'A quem essa palestra pertence'),
    )
    """
    Atributo da classe StandardItemStuffModel para
    referenciar um objeto da classe speaker

    Caracteristicas:
    ForeignKey
    verbose name: palestrante
    """

    title = models.CharField(
        verbose_name=_(u'Titulo'),
        help_text=_(u'Informe um titulo da palestra'),
        max_length=255
    )
    """
    Atributo da classe StandardItemStuffModel para
    setar um titulo

    Caracteristicas:
    CharField
    verbose name: Titulo
    max length: 255
    """

    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        help_text=_(u'Informe um slug para o titulo da palestra'),
        unique=True,
        null=True
    )

    summary = models.TextField(
        verbose_name=_(u'Sumário'),
        help_text=_(u'Descreva um sumário para sua palestra')
    )
    """
    Atributo da classe StandardItemStuffModel para
    setar um sumário

    Caracteristicas:
    TextField
    verbose name: Sumário
    """

    tags = TaggableManager()
    """
    Atributo da classe StandardItemStuffModel para
    setar as tags através do pacote django-taggit

    Caracteristicas:
    ManyToMany
    """

    class Meta:
        """
        Seta a classe como abstrata
        """
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
    """
    Atributo da classe Media para escolher as
    opcoes setada na tupla KINDS

    Caracteristicas:
    CharField
    max length: 2
    """

    title = models.CharField(
        verbose_name=_(u'Titulo'),
        max_length=255
    )
    """
    Atributo da classe Media para
    setar um titulo

    Caracteristicas:
    CharField
    verbose name: Titulo
    max length: 255
    """

    url = models.URLField(
        verbose_name=_('URL'),
    )
    """
    Atributo da classe Media para
    setar uma url valida

    Caracteristicas:
    UrlField
    verbose name: URL
    """

    class Meta:
        """
        Seta a classe como abstrata
        """
        abstract = True
