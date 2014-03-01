# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from rest_framework import generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Third-party app imports

# Imports from your apps
from .models import Speaker
from .serializers import SpeakerSerializer


class SpeakerList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestrantes, e permite que novos
    palestrantes sejam cadastrados.
    """
    model = Speaker
    serializer_class = SpeakerSerializer


class SpeakerDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia de palestrante, e permite que novos
    palestrantes sejam atualizados.
    '''
    model = Speaker
    serializer_class = SpeakerSerializer


class SpeakerListView(ListView):
    """
    Classe responsavel por gerar uma lista
    paginada com os palestrantes cadastrados
    no sistema.
    """

    model = Speaker
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
            Speaker.objects.all()
            .select_related('KindContact')
            .order_by('name')
        )


class SpeakerDetailView(DetailView):
    """
    Classe responsavel por gerar o detalhe
    da palestra
    """

    model = Speaker
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
