# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

# Third-party app imports
from model_mommy import mommy

# Relative imports of the 'app-name' package
from screencasts.models import Screencast, Serie, MediaScreencast

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


class SerieTest(TestCase):
    """
    Classe para testar o model Serie
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.serie = mommy.make(Serie)

    def test_serie_create_instance(self):
        """
        Testa se a instancia do model Serie foi criada
        """
        self.assertIsInstance(
            self.serie,
            Serie
        )

    def test_return_unicode_method(self):
        """
        Testa o retorno do metodo unicode
        """
        self.assertEqual(
            self.serie.name,
            self.serie.__unicode__()
        )


class ScreencastTestModel(TestCase):
    """
    Classe para testar o model
    Screencast
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.screencast = mommy.make(Screencast)

    def test_screencast_create_instance(self):
        """
        Testa se o model Screencast foi criado
        """
        self.assertIsInstance(
            self.screencast,
            Screencast
        )

    def test_return_get_absolute_url_method(self):
        """
        Testa se o metodo get_absolute_url
        esta fazendo o reverse correto para
        os detalhes do screencast
        """
        self.assertEqual(
            self.screencast.get_absolute_url(),
            reverse(
                'screencasts:screencast-detail-view',
                args=[self.screencast.slug]
            )
        )

    def test_return_unicode_method(self):
        """
        Testa o retorno do metodo unicode
        para ver se os campos estao corretos
        """
        self.assertEqual(
            self.screencast.__unicode__(),
            self.screencast.title
        )


class MediaScreencastTest(TestCase):
    """
    Classe para testar o model MediaScreencast
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.media = mommy.make(MediaScreencast)

    def test_mediascreencast_create_instance(self):
        """
        Testa se o model MediaScreencast foi criado
        """
        self.assertIsInstance(
            self.media,
            MediaScreencast
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
