# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.http import condition
from rest_framework import generics
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Third-party app imports

# Imports from your apps
from .models import Talk
# from .serializers import TalkSpeakerSerializer


class TalkList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestras, e permite que novos
    palestras sejam cadastradas.
    """
    model = Talk


class TalkDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia da palestra, e permite que novos
    palestras sejam atualizados.
    '''
    model = Talk


class TalkListView(ListView):
    u"""
    Classe responsavel por gerar uma lista
    paginada com as palestras cadastradas
    no sistema.
    """

    model = Talk
    u"""
    Define o model a ser atribuido
    """

    template_name = "talk_list.html"
    u"""
    Define o nome do template a ser utilizado
    """

    context_object_name = "talk_list"
    u"""
    Define o nome do objeto a ser renderizado
    no contexto da requisição
    """

    paginate_by = 10
    u"""
    Define o tamanho dos items a serem
    paginados
    """

    def get_queryset(self):
        u"""
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """
        return (
            Talk.objects.all()
            .select_related('MediaTalk')
            .order_by('title')
        )

    def latest_entry(request):
        u"""
        Metodo responsavel por retornar o ultimo objeto criado
        no model e setar nos cabecalhos de resposta do
        protocolo http.
        """
        return Talk.objects.latest('created').created

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
            TalkListView, self
        ).dispatch(request, *args, **kwargs)


class TalkDetailView(DetailView):
    u"""
    Classe responsavel por gerar o detalhe
    da palestra
    """

    model = Talk
    u"""
    Define o model a ser atribuido
    """

    template_name = "talk_detail.html"
    u"""
    Define o nome do template a ser utilizado
    """
