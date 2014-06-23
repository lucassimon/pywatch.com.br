# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

# Third-party app imports

# Imports from your apps
from talks.models import Talk
from screencasts.models import Screencast


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

        context['talks_count'] = (
            Talk.objects.filter(
                speaker=context.get('view').request.user
            ).count()
        )
        context['screencasts_count'] = (
            Screencast.objects.filter(
                speaker=context.get('view').request.user
            ).count()
        )
        # context['tutorials_count'] = (
        #     Talk.objects.filter(
        #         speaker=context.get('view').request.user
        #     ).count()
        # )
        return context
