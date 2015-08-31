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
from speakers.models import SpeakerUser
from screencasts.models import Screencast
from screencasts.forms import ScreencastForm, MediaScreencastFormSet


class ScreencastIndexTemplateView(TemplateView):
    u"""
    Classe generica para renderizar o template
    da index de videos no dashboard
    """

    template_name = "dashboards/screencasts/index.html"
    u"""
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
        return super(ScreencastIndexTemplateView, self).dispatch(
            *args,
            **kwargs
        )


class ScreencastCreateView(CreateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/screencasts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = ScreencastForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-screencast-list-view')
    """
    Define a url de sucesso apos criar o objeto de video
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(ScreencastCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        u"""
        Seta as variaveis do formset para o cotexto do formulário
        """
        context = super(ScreencastCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['mediascreencast_formset'] = MediaScreencastFormSet(
                self.request.POST
            )
        else:
            context['mediascreencast_formset'] = MediaScreencastFormSet()
        return context

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        context = self.get_context_data()
        mediascreencast_forms = context['mediascreencast_formset']

        screencast = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        screencast.slug = slugify(screencast.title)
        # adiciona no formulario screencast
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        screencast.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado
        screencast.save()
        super(ScreencastCreateView, self).form_valid(form)
        # chama o metodo super

        # salvar as medias no formulario
        if mediascreencast_forms.is_valid():
            for idx, media in enumerate(mediascreencast_forms):
                media_type, media_title, media_url = self.get_media_form_data(
                    media,
                    idx
                )
                if media_type and media_title and media_url:
                    media.save(commit=False)
                    media.instance.screencast = screencast
                    media.save()

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_media_form_data(self, media, idx):
        """
        Retorna os valores dos atributos do formset media screencast
        """
        mtype = media.data.get("form-%d-type" % idx, "")
        mtitle = media.data.get("form-%d-title" % idx, "")
        murl = media.data.get("form-%d-url" % idx, "")

        return mtype, mtitle, murl

    def get_form_kwargs(self):
        """
        Retorna o usuário corrente para o formulario
        """
        kwargs = super(ScreencastCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        return kwargs


class ScreencastUpdateView(UpdateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/screencasts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = ScreencastForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-screencast-list-view')
    """
    Define a url de sucesso apos criar o objeto de video
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(ScreencastUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = Screencast.objects.get(id=self.kwargs['pk'])
        return obj

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            screencast = Screencast.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar a video %s" % pk)
            )

        form = ScreencastForm(request.POST, instance=screencast)

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
        screencast = form.save(commit=False)
        # seta o commit do formulario como false

        from uuslug import slugify
        # importa o slugfy

        screencast.slug = slugify(screencast.title)
        # adiciona no formulario screencast
        # no atributo slug a chamada do metodo
        # slugify de acordo com o titulo
        # passado no formulario

        screencast.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado

        screencast.save()
        # salvar a o formulario

        super(ScreencastUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(ScreencastUpdateView, self).form_invalid(form)


class ScreencastListView(ListView):
    """
    Classe generica para listar as videos
    do usuário
    """

    template_name = "dashboards/screencasts/list.html"
    """
    Define o nome do template a ser utilizado
    """
    model = Screencast

    context_object_name = "screencast_list"
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
        return super(ScreencastListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            ScreencastListView, self
        ).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            Screencast.objects.filter(
                speaker=self.request.user
            )
        )


class ScreencastDeleteView(DeleteView):
    u"""
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/screencasts/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = Screencast
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-screencast-list-view')
    u"""
    Define a url de sucesso apos criar o objeto de video
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(ScreencastDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = Screencast.objects.get(id=self.kwargs['pk'])
        return obj
