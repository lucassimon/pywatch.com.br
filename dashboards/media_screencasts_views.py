# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
from screencasts.models import MediaScreencast
from screencasts.forms import MediaScreencastCreateAndUpdateForm


class MediaScreencastIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/mediascreencasts/index.html"
    """
    Define o nome do template a ser utilizado
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(MediaScreencastIndexTemplateView, self).dispatch(
            *args,
            **kwargs
        )


class MediaScreencastCreateView(CreateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediascreencasts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = MediaScreencastCreateAndUpdateForm
    """
    Define o formulario a ser renderizado no template
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(MediaScreencastCreateView, self).dispatch(
            *args,
            **kwargs
        )

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para salvar
        o slug field
        """
        mediascreencast = form.save(commit=False)
        # seta o commit do formulario como false

        mediascreencast.save()
        # salvar a o formulario

        super(MediaScreencastCreateView, self).form_valid(form)
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
            'dashboards:dashboard-mediascreencast-list-view',
            kwargs={'screencast_pk': self.kwargs.get('screencast_pk')},
        )


class MediaScreencastUpdateView(UpdateView):
    """
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediascreencasts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = MediaScreencastCreateAndUpdateForm
    """
    Define o formulario a ser renderizado no template
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(MediaScreencastUpdateView, self).dispatch(
            *args,
            **kwargs
        )

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar o evento
        de acordo com o id dela
        """
        return MediaScreencast.objects.get(id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            mediascreencast = MediaScreencast.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar o evento %s" % pk)
            )

        form = MediaScreencastCreateAndUpdateForm(
            request.POST,
            instance=mediascreencast
        )

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
        mediascreencast = form.save(commit=False)
        # seta o commit do formulario como false

        mediascreencast.save()
        # salvar a o formulario

        super(MediaScreencastUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(MediaScreencastUpdateView, self).form_invalid(form)

    def get_success_url(self):
        """
        Define a url de sucesso apos criar o objeto de evento
        """
        return reverse_lazy(
            'dashboards:dashboard-mediascreencast-list-view',
            kwargs={'screencast_pk': self.kwargs.get('screencast_pk')},
        )


class MediaScreencastListView(ListView):
    """
    Classe generica para listar os eventos
    do usuário
    """

    template_name = "dashboards/mediascreencasts/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = MediaScreencast

    context_object_name = "media_screencast_list"
    """
    Define o nome do objeto a ser renderizado
    no contexto da requisição
    """

    paginate_by = 10
    """
    Define o tamanho dos items a serem
    paginados
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(MediaScreencastListView, self).dispatch(
            *args,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            MediaScreencastListView, self
        ).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            MediaScreencast.objects.filter(
                screencast__speaker=self.request.user,
                screencast=self.kwargs.get('screencast_pk')
            )
        )


class MediaScreencastDeleteView(DeleteView):
    u"""
    Classe generica para criar os eventos
    do usuário
    """
    template_name = "dashboards/mediascreencasts/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = MediaScreencast
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy(
        'dashboards:dashboard-mediascreencast-list-view'
    )
    u"""
    Define a url de sucesso apos criar o objeto de evento
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(MediaScreencastDeleteView, self).dispatch(
            *args,
            **kwargs
        )

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a evento
        de acordo com o id dela
        """
        obj = MediaScreencast.objects.get(id=self.kwargs['pk'])
        return obj
