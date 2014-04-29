# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from rest_framework import generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Third-party app imports

# Imports from your apps
from .models import Screencast


class ScreencastList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestras, e permite que novos
    palestras sejam cadastradas.
    """
    model = Screencast


class ScreencastDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia da palestra, e permite que novos
    palestras sejam atualizados.
    '''
    model = Screencast


class ScreencastListView(ListView):
    """
    Classe responsavel por gerar uma lista
    paginada com as palestras cadastradas
    no sistema.
    """

    model = Screencast
    """
    Define o model a ser atribuido
    """

    template_name = "screencast_list.html"
    """
    Define o nome do template a ser utilizado
    """

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

    def get_queryset(self):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            Screencast.objects.all()
            .select_related('MediaScreencast')
            .order_by('title')
        )


class ScreencastDetailView(DetailView):
    """
    Classe responsavel por gerar o detalhe
    da palestra
    """

    model = Screencast
    """
    Define o model a ser atribuido
    """

    template_name = "screencast_detail.html"
    """
    Define o nome do template a ser utilizado
    """
