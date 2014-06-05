# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext as _

# Relative imports of the 'app-name' package


class SpeakerQueryset(models.query.QuerySet):
    """
    Classe para definir os querysets do model palestrante
    """
    def latest_with_limits(self, l):
        """
        :param l: Número para limitar a busca
        """
        return self.order_by("-created")[:l]


class SpeakerManager(BaseUserManager, models.Manager):
    """
    Define um manager para o model de palestrantes
    """
    def get_queryset(self):
        return SpeakerQueryset(self.model, using=self._db)

    def create_user(
        self,
        first_name,
        last_name,
        email,
        bio,
        password=None,
        **extra_fields
    ):
        """
        Cria e salva um usuário com o email passado e senha
        """
        if not email:
            raise ValueError(_(u'Usuários devem possuir um email'))

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            email=SpeakerManager.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        first_name,
        last_name,
        email,
        bio,
        password=None,
        **extra_fields
    ):
        """
        Cria e salva um super-usuário com o email passado e senha
        """

        user = self.create_user(
            first_name,
            last_name,
            email,
            bio,
            password,
            **extra_fields
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def latest_with_limits(self, limit):
        """
        Retorna os ultimos palestrantes
        de acordo com o limit setado
        :param limit: Integer seta o limite da busca
        """
        return self.get_queryset().latest_with_limits(limit)
