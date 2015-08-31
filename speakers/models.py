# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser
from django.views.generic.edit import CreateView

# Realative imports of the 'app-name' package
from core.models import TimeStampedModel
from .managers import SpeakerManager


class SpeakerUser(AbstractUser, TimeStampedModel):
    """
    Classe model para criar um objeto model
    de palestrante.
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'bio']

    slug = models.SlugField(
        verbose_name=_(u'Slug'),
        db_index=True,
        max_length=255,
        null=True,
        blank=True
    )
    """
    Atributo da classe Speaker para setar o slug
    do palestrante.

    Caracteristicas:
    max length: 255
    index: True
    unique: True
    """

    bio = models.TextField(
        verbose_name=_(u'Biográfia'),
        blank=True,
        null=True,
        default=''
    )
    """
    Atributo da classe Speaker para setar a biografria
    do palestrante.

    Caracteristicas:
    TextField
    """

    is_admin = models.BooleanField(
        verbose_name=_(u'Administrador'),
        default=False,
        help_text=_(u'Designa este usuário como administrador.')
    )
    """
    Atributo da classe Speaker para
    setar o palestrante como administrador.

    Caracteristicas:
    BooleanField
    Default: False
    """

    objects = SpeakerManager()

    def get_absolute_url(self):
        """
        Retorna o caminho absoluto da instancia
        do objeto, através do reverse
        usando namespace definido no arquivo
        urls.py
        """
        return reverse('speakers:speaker-detail-view', args=[self.slug])

    def get_full_name(self):
        """
        Retorna o primeiro nome mais o ultimo nome, com
        um espaço entre eles
        """
        full_name = u'%s %s' % (
            self.first_name,
            self.last_name
        )
        return full_name.strip()

    def get_short_name(self):
        """
        Retorna somente o primeiro nome
        """
        return u'%s' % (self.first_name)

    def save(self, *args,  **kwargs):
        """
        Customiza o metodo salvar da classe
        para guardar o slug do palestrante
        """
        from uuslug import uuslug as slugify
        if not self.first_name:
            self.first_name = 'speaker noname'
        slug_str = "%s %s" % (self.first_name, self.last_name)

        self.slug = slugify(slug_str, instance=self, start_no=1)
        super(SpeakerUser, self).save(**kwargs)

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
        return u'%s' % (self.get_full_name())


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
        ('ST', _('Site')),
        ('BL', _('Blog')),
    )

    speaker = models.ForeignKey(
        'SpeakerUser',
        verbose_name=_('Palestrante'),
        related_name='contacts'
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
