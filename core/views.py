# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.views.generic import TemplateView

# Third-party app imports

# Imports from your apps


class IndexHomePageTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index
    """

    template_name = "index.html"
    """
    Define o nome do template a ser utilizado
    """
