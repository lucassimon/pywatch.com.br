# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase
from django.core.urlresolvers import reverse


# ######## WHAT WE NEED TEST #########
#
# 1 - viewing of data / visualizacao de dados
# 2 - changing of data / mudanca de dados
# 3 - custom class-based-views methods / metodos customizados

# ############ TIPS ##################
#
# 1 - Cada função de test deve haver apenas 1 assert
#
# ####################################


class SpeakerListViewTest(TestCase):
    """
    Testa as views da app speaker
    """

    def setUp(self):
        """
        Inicializa os testes
        """
        pass

    def test_response_200_on_get(self):
        """
        Testa se o status de resposta e 200
        """
        pass

    def test_template_used(self):
        """
        Testa se o template usado
        é o speaker_list.html
        """
        pass
