# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
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


class EventTest(TestCase):
    """
    Classe para testar o model Event na app de talks
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.event = mommy.make(Event)



class TalkTestModel(TestCase):
    """
    Classe para testar o model Talk na app talks
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.talk = mommy.make(Talk)


class MediaTalkTest(TestCase):
    """
    Classe para testar o model MediaTalk na app talks
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.mediatalk = mommy.make(MediaTalk)
        self.media = mommy.make(MediaTalk)

    def test_mediatalk_create_instance(self):
        """
        Testa se o model MediaTalk foi criado
        """
        self.assertIsInstance(
            self.media,
            MediaTalk
        )

    def test_return_unicode_method(self):
        """
        Testa o retorno do metodo unicode
        para ver se os campos estao corretos
        """
        self.assertEqual(
            self.media.__unicode__(),
            u'%s - %s' % (
                self.media.title,
                self.media.url
            )
        )
