# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from speakers.models import SpeakerUser, KindContact

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
#####################################


class SpeakerTestModel(TestCase):
    """
    Classe para testar o model
    Speaker
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.speaker = mommy.make(SpeakerUser)

    def test_speaker_create_instance(self):
        """
        Testa se o model Speaker foi criado
        """
        self.assertIsInstance(self.speaker, SpeakerUser)

    def test_return_unicode_method(self):
        """
        Testa o retorno do metodo unicode
        para ver se os campos estao corretos
        """
        self.assertEqual(
            self.speaker.__unicode__(),
            self.speaker.get_full_name()
        )

    def test_return_three_most_recent_created(self):
        """
        Testa se ira trazer os 3 palestrantes mais
        recentes criados
        """

        # self.speaker = mommy.make(SpeakerUser, name='speaker-1')
        # self.speaker_two = mommy.make(SpeakerUser, name='speaker-2')
        # self.speaker_three = mommy.make(SpeakerUser, name='speaker-3')
        # self.speaker_four = mommy.make(SpeakerUser, name='speaker-4')
        # self.speaker_five = mommy.make(SpeakerUser, name='speaker-5')
        # self.speaker_six = mommy.make(SpeakerUser, name='speaker-6')

        # qs = Speaker.objects.all().order_by('-created')[:3]
        # self.assertQuerysetEqual(
        # qs,
        # [
        # "<Speaker: speaker-6>",
        # "<Speaker: speaker-5>",
        # "<Speaker: speaker-4>"
        # ]
        # )
        pass

    def test_return_latest_three_most_recent_created_manager(self):
        """
        Testa o manager most recent recent created
        """
        pass


class KindContactTest(TestCase):
    """
    Classe para testar o model KindContact
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.speaker = Recipe(
            SpeakerUser,
            first_name='joao silva',
            bio='lorem ipsum dolor'
        )

        self.kind_contact = Recipe(
            KindContact,
            speaker=foreign_key(self.speaker),
            kind='PH',
            value='9999999999999'
        )

    def test_kind_contact_create_instance(self):
        """
        Testa se o model KindContact foi criado
        """
        kind_contact = self.kind_contact.make()
        self.assertIsInstance(kind_contact, KindContact)
