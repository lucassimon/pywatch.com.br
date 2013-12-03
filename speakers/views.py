# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from rest_framework import generics

# Third-party app imports

# Imports from your apps
from .models import Speaker


class SpeakerList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestrantes, e permite que novos
    palestrantes sejam cadastrados.
    """
    model = Speaker


class SpeakerDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia de palestrante, e permite que novos
    palestrantes sejam atualizados.
    '''
    model = Speaker
