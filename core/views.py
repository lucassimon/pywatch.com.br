# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.views.generic import TemplateView

# Third-party app imports

# Imports from your apps
from speakers.models import Speaker
from talks.models import Talk


class IndexHomePageTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index
    """

    template_name = "index.html"
    """
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            IndexHomePageTemplateView, self
        ).get_context_data(**kwargs)
        context['most_recent_speakers_list'] = (
            Speaker.objects.latest_with_limits(5)
        )
        context['most_recent_talks_list'] = (
            Talk.objects.latest_with_limits(5)
        )
        return context
