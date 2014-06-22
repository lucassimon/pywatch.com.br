# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

# Third-party app imports

# Imports from your apps


class DashboardIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index no dashboard
    """

    template_name = "dashboards/index.html"
    """
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            DashboardIndexTemplateView, self
        ).get_context_data(**kwargs)
        return context
