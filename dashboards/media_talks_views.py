# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
from speakers.models import SpeakerUser
from talks.models import MediaTalk
from talks.forms import MediaTalkCreateAndUpdateForm


class MediaTalkIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/mediatalks/index.html"
    """
    Define o nome do template a ser utilizado
    """


class MediaTalkCreateView(CreateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediatalks/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = MediaTalkCreateAndUpdateForm
    """
    Define o formulario a ser renderizado no template
    """

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para salvar
        o slug field
        """
        mediatalk = form.save(commit=False)
        # seta o commit do formulario como false

        mediatalk.save()
        # salvar a o formulario

        super(MediaTalkCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_success_url(self):
        """
        Define a url de sucesso apos criar o objeto de evento
        """
        return reverse_lazy(
            'dashboards:dashboard-mediatalk-list-view',
            kwargs={'talk_pk': self.kwargs.get('talk_pk')},
        )


class MediaTalkUpdateView(UpdateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediatalks/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = MediaTalkCreateAndUpdateForm
    """
    Define o formulario a ser renderizado no template
    """

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar o evento
        de acordo com o id dela
        """
        return MediaTalk.objects.get(id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            mediatalk = MediaTalk.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar o evento %s" % pk)
            )

        form = MediaTalkCreateAndUpdateForm(request.POST, instance=mediatalk)

        if form.is_valid():
            self.form_valid(form)
            # e retorna para a página de sucesso
            return HttpResponseRedirect(
                self.get_success_url()
            )
        else:
            self.form_invalid(form)
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        u"""
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        mediatalk = form.save(commit=False)
        # seta o commit do formulario como false

        mediatalk.save()
        # salvar a o formulario

        super(MediaTalkUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(MediaTalkUpdateView, self).form_invalid(form)

    def get_success_url(self):
        """
        Define a url de sucesso apos criar o objeto de evento
        """
        return reverse_lazy(
            'dashboards:dashboard-mediatalk-list-view',
            kwargs={'talk_pk': self.kwargs.get('talk_pk')},
        )


class MediaTalkListView(ListView):
    """
    Classe generica para listar os eventos
    do usuário
    """

    template_name = "dashboards/mediatalks/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = MediaTalk

    context_object_name = "media_talk_list"
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
            MediaTalkListView, self
        ).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            MediaTalk.objects.filter(
                talk__speaker=self.request.user,
                talk=self.kwargs.get('talk_pk')
            )
        )


class MediaTalkDeleteView(DeleteView):
    u"""
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediatalks/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = MediaTalk
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-mediatalk-list-view')
    u"""
    Define a url de sucesso apos criar o objeto de evento
    """

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a evento
        de acordo com o id dela
        """
        obj = MediaTalk.objects.get(id=self.kwargs['pk'])
        return obj
