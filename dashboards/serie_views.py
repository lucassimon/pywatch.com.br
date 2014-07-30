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
from screencasts.models import Serie
from screencasts.forms import SerieForm


class SerieIndexTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index da series de videos no dashboard
    """

    template_name = "dashboards/series/index.html"
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
        return super(SerieIndexTemplateView, self).dispatch(*args, **kwargs)


class SerieCreateView(CreateView):
    """
    Classe generica para criar as series
    dos videos do usuario
    """
    template_name = "dashboards/series/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SerieForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-serie-list-view')
    """
    Define a url de sucesso apos criar o objeto da serie
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(SerieCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para salvar
        o slug field
        """
        serie = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        serie.slug = slugify(serie.name)
        # adiciona no formulario talk
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        serie.save()
        # salvar a o formulario

        super(SerieCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )


class SerieUpdateView(UpdateView):
    """
    Classe generica para criar as series
    dos videos do usuário
    """
    template_name = "dashboards/series/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SerieForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-serie-list-view')
    """
    Define a url de sucesso apos criar o objeto da serie
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(SerieUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a serie
        de acordo com o id dela
        """
        return Serie.objects.get(id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            serie = Serie.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar a série %s" % pk)
            )

        form = SerieForm(request.POST, instance=serie)

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
        serie = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        serie.slug = slugify(serie.name)
        # adiciona no formulario serie
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        serie.save()
        # salvar a o formulario

        super(SerieUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(SerieUpdateView, self).form_invalid(form)


class SerieListView(ListView):
    """
    Classe generica para listar as series
    dos videos do usuário
    """

    template_name = "dashboards/series/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = Serie

    context_object_name = "serie_list"
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
        return super(SerieListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            SerieListView, self
        ).get_context_data(**kwargs)
        context['serie_list'] = Serie.objects.all()

        return context


class SerieDeleteView(DeleteView):
    u"""
    Classe generica para deletar as series de videos
    do usuário
    """
    template_name = "dashboards/series/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = Serie
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-serie-list-view')
    u"""
    Define a url de sucesso apos criar o objeto da serie
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(SerieDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a serie
        de acordo com o id dela
        """
        obj = Serie.objects.get(id=self.kwargs['pk'])
        return obj
