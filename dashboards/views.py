# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

# Third-party app imports

# Imports from your apps
from speakers.models import SpeakerUser
from talks.models import Talk
from talks.forms import TalkForm
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


class TalkCreateView(CreateView):
    """
    Classe generica para criar as palestras
    do usuário
    """
    template_name = "dashboards/talks/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = TalkForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-talk-list-view')
    """
    Define a url de sucesso apos criar o objeto de palestra
    """

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        talk = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        talk.slug = slugify(talk.title)
        # adiciona no formulario talk
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        talk.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado

        talk.save()
        # salvar a o formulario

        super(TalkCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_form_kwargs(self):
        """
        Retorna o usuário corrente para o formulario
        """
        kwargs = super(TalkCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        return kwargs


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
