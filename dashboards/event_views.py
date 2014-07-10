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
from talks.models import Event
from talks.forms import EventForm


class EventIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/events/index.html"
    """
    Define o nome do template a ser utilizado
    """


class EventCreateView(CreateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/events/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = EventForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-talk-create-view')
    """
    Define a url de sucesso apos criar o objeto de evento
    """

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para salvar
        o slug field
        """
        event = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        event.slug = slugify(event.name)
        # adiciona no formulario talk
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        event.save()
        # salvar a o formulario

        super(EventCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )


class EventUpdateView(UpdateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/events/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = EventForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-event-list-view')
    """
    Define a url de sucesso apos criar o objeto de evento
    """

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar o evento
        de acordo com o id dela
        """
        return Event.objects.get(id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            event = Event.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar o evento %s" % pk)
            )

        form = EventForm(request.POST, instance=event)

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
        event = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        event.slug = slugify(event.name)
        # adiciona no formulario event
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        event.save()
        # salvar a o formulario

        super(EventUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(EventUpdateView, self).form_invalid(form)


class EventListView(ListView):
    """
    Classe generica para listar os eventos
    do usuário
    """

    template_name = "dashboards/events/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = Event

    context_object_name = "event_list"
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
            EventListView, self
        ).get_context_data(**kwargs)
        context['event_list'] = Event.objects.all()

        return context


class EventDeleteView(DeleteView):
    u"""
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/events/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = Event
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-event-list-view')
    u"""
    Define a url de sucesso apos criar o objeto de evento
    """

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a evento
        de acordo com o id dela
        """
        obj = Event.objects.get(id=self.kwargs['pk'])
        return obj
