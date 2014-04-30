# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models

# Relative imports of the 'app-name' package


class TalkQueryset(models.query.QuerySet):
    """
    Classe para definir os querysets do model palestras
    """
    def latest_with_limits(self, l):
        """
        :param l: Número para limitar a busca
        """
        return self.order_by("-created")[:l]


class TalkManager(models.Manager):
    """
    Define um manager para o model de palestras
    """
    def get_queryset(self):
        return TalkQueryset(self.model, using=self._db)

    def latest_with_limits(self, limit):
        """
        Retorna os ultimos palestrantes
        de acordo com o limit setado
        :param limit: Integer seta o limite da busca
        """
        return self.get_queryset().latest_with_limits(limit)
