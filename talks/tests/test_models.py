# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from talks.models import Event, Talk, MediaTalk


# ######## WHAT WE NEED TEST #########
#
# 1 - creating / criação
# 2 - reading / leitura
# 3 - updating / atualização
# 4 - deleting / deleção
# 5 - model methods / metodos do model
# 6 - model managers / não ha tradução para isto
# 7 - model managers methods / não ha tradução para isto

# ############ TIPS ##################
#
# 1 - Cada função de test deve haver apenas 1 assert
#
# ####################################


class EventTestModel(TestCase):
    """
    Classe para testar o model
    Event
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.event = mommy.make(Event)


class TalkTestModel(TestCase):
    """
    Classe para testar o model
    Talk
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.talk = mommy.make(Talk)


class MediaTalkTestModel(TestCase):
    """
    Classe para testar o model
    MediaTalk
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.mediatalk = mommy.make(MediaTalk)
