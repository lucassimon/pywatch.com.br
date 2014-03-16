from django_webtest import WebTest
from django.core.urlresolvers import reverse


class TestTalkListViewPage(WebTest):
    """
    Feature: Exibir as palestras

    Cenario: Como usuario do site
    Dado Eu acesso a url /palestras/
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
