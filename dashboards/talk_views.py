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
from talks.models import Talk
from talks.forms import TalkForm, MediaTalkFormSet


class TalkIndexTemplateView(TemplateView):
    u"""
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "dashboards/talks/index.html"
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
        return super(TalkIndexTemplateView, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(TalkCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        u"""
        Seta as variaveis do formset para o cotexto do formulário
        """
        context = super(TalkCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['mediatalk_formset'] = MediaTalkFormSet(self.request.POST)
        else:
            context['mediatalk_formset'] = MediaTalkFormSet()
        return context

    def form_valid(self, form):
        """
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        context = self.get_context_data()
        mediatalk_forms = context['mediatalk_formset']

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
        super(TalkCreateView, self).form_valid(form)
        # chama o metodo super

        # salvar as medias no formulario
        if mediatalk_forms.is_valid():
            for idx, media in enumerate(mediatalk_forms):
                media_type, media_title, media_url = self.get_media_form_data(
                    media,
                    idx
                )
                if media_type and media_title and media_url:
                    media.save(commit=False)
                    media.instance.talk = talk
                    media.save()

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_media_form_data(self, media, idx):
        """
        Retorna os valores dos atributos do formset media talk
        """
        mtype = media.data.get("form-%d-type" % idx, "")
        mtitle = media.data.get("form-%d-title" % idx, "")
        murl = media.data.get("form-%d-url" % idx, "")

        return mtype, mtitle, murl

    def get_form_kwargs(self):
        """
        Retorna o usuário corrente para o formulario
        """
        kwargs = super(TalkCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        return kwargs


class TalkUpdateView(UpdateView):
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(TalkUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a palestra
        de acordo com o id dela
        """
        obj = Talk.objects.get(id=self.kwargs['pk'])
        return obj

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            talk = Talk.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar a palestra %s" % pk)
            )

        form = TalkForm(request.POST, instance=talk)

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

        super(TalkUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(TalkUpdateView, self).form_invalid(form)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(TalkListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            TalkListView, self
        ).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            Talk.objects.filter(
                speaker=self.request.user
            )
        )


class TalkDeleteView(DeleteView):
    u"""
    Classe generica para criar as palestras
    do usuário
    """
    template_name = "dashboards/talks/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = Talk
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('dashboards:dashboard-talk-list-view')
    u"""
    Define a url de sucesso apos criar o objeto de palestra
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(TalkDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a palestra
        de acordo com o id dela
        """
        obj = Talk.objects.get(id=self.kwargs['pk'])
        return obj
