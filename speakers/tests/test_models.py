# -*- coding:utf-8 -*-

# Core Django imports
from django.test import TestCase
from django.core.urlresolvers import reverse

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, seq

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
    Classe para testar o model Speaker na app speakers
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.speaker = mommy.make(
            SpeakerUser,
            first_name='Jhon',
            last_name='Dhoe'
        )

    def test_speaker_create_instance(self):
        """
        Testa se o model Speaker foi criado
        """
        self.assertIsInstance(self.speaker, SpeakerUser)

    def test_return_get_absolute_url_method(self):
        """
        Testa se o metodo get_absolute_url
        esta fazendo o reverse correto para
        os detalhes do palestrante
        """
        self.assertEqual(
            self.speaker.get_absolute_url(),
            reverse(
                'speakers:speaker-detail-view',
                args=[self.speaker.slug]
            )
        )

    def test_return_get_full_name_method(self):
        u"""
        Testa o retorno do metodo get_full_name
        e se esta retornando o nome e o sobrenome concatenados
        corretamente
        """
        self.assertEqual(
            self.speaker.get_full_name(),
            u'%s %s' % (
                self.speaker.first_name,
                self.speaker.last_name
            )
        )

    def test_return_get_short_name_method(self):
        u"""
        Teste o retorno do metodo get_short_name
        esta trazendo o primeiro nome do palestrante
        usuario
        """
        self.assertEqual(
            self.speaker.get_short_name(),
            u'%s' % self.speaker.first_name
        )

    def test_method_save_speaker(self):
        u"""
        Testa e o metodo save esta salvando o slug
        do palestrante de acordo com o primeiro
        nome e segundo nome
        """
        self.speaker.first_name = u'Ashely'
        self.speaker.last_name = u' Cole Jr'
        self.speaker.save()
        from uuslug import slugify
        slug_str = "%s %s" % (
            self.speaker.first_name,
            self.speaker.last_name
        )
        slug = slugify(slug_str)
        self.assertEqual(
            self.speaker.slug,
            slug
        )

    def test_return_unicode_method(self):
        u"""
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
        speaker_1 = mommy.make(
            SpeakerUser,
            first_name='Jhon',
            last_name='Doe'
        )
        speaker_2 = mommy.make(
            SpeakerUser,
            first_name='Jhon2',
            last_name='Doe2'
        )
        speaker_3 = mommy.make(
            SpeakerUser,
            first_name='Jhon3',
            last_name='Doe3'
        )
        speaker_4 = mommy.make(
            SpeakerUser,
            first_name='Jhon4',
            last_name='Doe4'
        )
        self.assertListEqual(
            list(SpeakerUser.objects.latest_with_limits(3)),
            [
                speaker_4,
                speaker_3,
                speaker_2
            ]
        )


class KindContactTest(TestCase):
    """
    Classe para testar o model KindContact na apps speakers
    """

    def setUp(self):
        """
        Metodo para inicializar os testes
        """
        self.kind = mommy.make(KindContact)

    def test_kind_contact_create_instance(self):
        """
        Testa se o model KindContact foi criado
        """
        self.assertIsInstance(
            self.kind,
            KindContact
        )

    def test_return_unicode_method(self):
        """
        Testa se o retorno do metodo unicode esta correto
        """
        self.assertEqual(
            self.kind.__unicode__(),
            u'%s, %s' % (
                self.kind.kind,
                self.kind.value
            )
        )
