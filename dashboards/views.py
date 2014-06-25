# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic import ListView

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


class TalkIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/talks/index.html"
    """
    Define o nome do template a ser utilizado
    """


class TalkListView(ListView):
    """
    Classe generica para listar as palestras
    do usuário
    """

    template_name = "dashboards/talks/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = Talk

    context_object_name = "talk_list"
    """
    Define o nome do objeto a ser renderizado
    no contexto da requisição
    """

    paginate_by = 10
    """
    Define o tamanho dos items a serem
    paginados
    """

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            TalkListView, self
        ).get_context_data(**kwargs)
        context['talk_list'] = Talk.objects.filter(
            speaker=context.get('view').request.user
        )

        return context


class ScreencastIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/screencasts/index.html"
    """
    Define o nome do template a ser utilizado
    """
