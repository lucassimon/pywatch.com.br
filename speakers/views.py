# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.http import condition
from django.views.generic.base import TemplateView
from rest_framework import generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
from .models import SpeakerUser, KindContact
from .serializers import SpeakerSerializer
from .forms import (
    SpeakerBasicInformationForm,
    SpeakerContactForm
)


class SpeakerList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestrantes, e permite que novos
    palestrantes sejam cadastrados.
    """
    model = SpeakerUser
    serializer_class = SpeakerSerializer


class SpeakerDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia de palestrante, e permite que novos
    palestrantes sejam atualizados.
    '''
    model = SpeakerUser
    serializer_class = SpeakerSerializer


class SpeakerProfileTemplateView(TemplateView):
    u"""
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "profile.html"
    u"""
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        u"""
        Seta váriaveis para o contexto
        """
        context = super(SpeakerProfileTemplateView, self).get_context_data(
            **kwargs
        )
        context['basic_information_form'] = SpeakerBasicInformationForm(
            instance=self.request.user
        )
        context['contact_list'] = KindContact.objects.filter(
            speaker=self.request.user
        )

        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(SpeakerProfileTemplateView, self).dispatch(
            *args,
            **kwargs
        )


class SpeakerListView(ListView):
    """
    Classe responsavel por gerar uma lista
    paginada com os palestrantes cadastrados
    no sistema.
    """

    model = SpeakerUser
    """
    Define o model a ser atribuido
    """

    template_name = "speaker_list.html"
    """
    Define o nome do template a ser utilizado
    """

    context_object_name = "speaker_list"
    """
    Define o nome do objeto a ser renderizado
    no contexto da requisição
    """

    paginate_by = 10
    """
    Define o tamanho dos items a serem
    paginados
    """

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            SpeakerUser.objects.all()
            .select_related('KindContact')
            .order_by('first_name')
            .exclude(username='root')
        )

    def latest_entry(request):
        u"""
        Metodo responsavel por retornar o ultimo objeto criado
        no model e setar nos cabecalhos de resposta do
        protocolo http.
        """
        return SpeakerUser.objects.latest('created').created

    @cache_control(max_age=600)
    @method_decorator(condition(last_modified_func=latest_entry))
    def dispatch(self, request, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(
            SpeakerListView, self
        ).dispatch(request, *args, **kwargs)


class SpeakerDetailView(DetailView):
    """
    Classe responsavel por gerar o detalhe
    da palestra
    """

    model = SpeakerUser
    """
    Define o model a ser atribuido
    """

    template_name = "speaker_detail.html"
    """
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        return context


def save_basic_information_profile(request):
    u"""
    Função responsável por salvar os dados do formulário
    exibidos na página de perfil do dashboard.
    """
    form = SpeakerBasicInformationForm(
        request.POST or None,
        instance=request.user
    )

    if form.is_valid():
        form.save()

    return HttpResponseRedirect(
        reverse('speakers:speaker-profile-view'),
        {'basic_information_form': form}
    )


class KindContactCreateView(CreateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/kindcontacts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SpeakerContactForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
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
        return super(KindContactCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        u"""
        Seta as variaveis do formset para o cotexto do formulário
        """
        context = super(KindContactCreateView, self).get_context_data(
            **kwargs
        )
        return context

    def form_valid(self, form):
        u"""
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        contact = form.save(commit=False)
        # seta o commit do formulario como false

        contact.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado
        contact.save()
        super(KindContactCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_form_kwargs(self):
        u"""
        Retorna o usuário corrente para o formulario
        """
        kwargs = super(KindContactCreateView, self).get_form_kwargs()
        return kwargs


class KindContactUpdateView(UpdateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/kindcontacts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SpeakerContactForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
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
        return super(KindContactUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = KindContact.objects.get(id=self.kwargs['pk'])
        return obj

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            contact = KindContact.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar este contato %s" % pk)
            )

        form = SpeakerContactForm(request.POST, instance=contact)

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
        contact = form.save(commit=False)
        # seta o commit do formulario como false

        contact.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado

        contact.save()
        # salvar a o formulario

        super(KindContactUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(KindContactUpdateView, self).form_invalid(form)


class KindContactDeleteView(DeleteView):
    u"""
    Classe generica para deletar os contatos do palestrante
    """
    template_name = "dashboards/kindcontacts/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = KindContact
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
    u"""
    Define a url de sucesso apos deletar o objeto
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(KindContactDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = KindContact.objects.get(id=self.kwargs['pk'])
        return obj
