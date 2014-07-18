# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from rest_framework import generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Third-party app imports

# Imports from your apps
from .models import SpeakerUser
from .serializers import SpeakerSerializer
from .forms import (
    SpeakerBasicInformationForm,
    ContactFormSet
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
        context['contact_form_set'] = ContactFormSet(
            instance=self.request.user
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
