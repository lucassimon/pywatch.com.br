#-*- coding:utf-8 -*-

#Core Django imports
from django_webtest import WebTest
from django.core.urlresolvers import reverse

#Third-party app imports
from model_mommy import mommy

# Relative imports of the 'app-name' package
from talks.models import Talk


class TestTalkListViewPage(WebTest):
    """
    Feature: Exibir as palestras

    Cenario: Como usuario do site
    Dado que um usuario acessa a url /palestras/
    Entao Eu vejo a lista de palestras
    """

    def test_show_list_talks_return_code_200(self):
        """
        Testa a exibicao das palestras retornando status code 200
        """
        talks = self.app.get(
            reverse('talks:talk-list-view')
        )
        assert talks.status_int == 200

    def test_show_list_talks_should_be_title_palestras(self):
        """
        Testa a exibicao das palestras e devera ter um titulo de palestras
        """
        talks = self.app.get(
            reverse('talks:talk-list-view')
        )
        assert '<h1> Palestras </h1>' in talks

    def test_show_list_talks_should_be_no_talks(self):
        """
        Testa a exibicao das palestras não ha nenhum resultado
        """
        talks = self.app.get(
            reverse('talks:talk-list-view')
        )
        assert '<p>Nenhuma palestra encontrada!!! :(</p>' in talks

    def test_show_list_talks_should_be_has_a_talk(self):
        """
        Testa a exibicao das palestras e se contem uma palestra
        """
        talks = self.app.get(
            reverse('talks:talk-list-view')
        )
        assert '<p>Nenhuma palestra encontrada!!! :(</p>' in talks
