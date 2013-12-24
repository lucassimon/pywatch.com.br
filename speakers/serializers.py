# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from rest_framework import serializers

# Third-party app imports

# Imports from your apps
from .models import Speaker, KindContact


class KindContactSerializer(serializers.ModelSerializer):
    """
    Serializar o model KindContact
    """
    kind_display = serializers.Field(
        source='get_kind_display',
    )

    class Meta:
        model = KindContact
        fields = ['kind', 'kind_display', 'value']


class SpeakerSerializer(serializers.ModelSerializer):
    """
    Serializar o model Speaker
    adicionando algumas funcionalidades
    na api
    """

    contacts = KindContactSerializer(many=True)

    class Meta:
        """
        Seta definições para serializar
        o model
        """
        model = Speaker
        fields = ['name', 'bio', 'contacts']

    def validate_bio(self, attrs, source):
        if len(attrs['bio']) < 5:
            raise serializers.ValidationError(
                u'Digite 5 letras ou mais.'
            )
        return attrs


class SpeakerSerializerManual(serializers.Serializer):
    """
    Cria um serializer manual
    caso os dados venham de outros lugares
    """
    name = serializers.CharField()
    slug = serializers.SlugField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.name = attrs.get('name', instance.name)
            instance.slug = attrs.get('slug', instance.slug)
            return instance
        return Speaker(**attrs)
