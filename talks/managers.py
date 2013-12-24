# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models


class TalkMostRecentCreatedManager(models.Manager):
    """
    Manager responsavel por trazer os
    palestras criados recentemente
    """

    def latest_with_limits(self, limit):
        """
        Retorna os ultimos palestrantes
        de acordo com o limit setado
        :param limit: Integer seta o limite da busca
        """
        self.limit = limit
        return self.order_by("-created")[:self.limit]
