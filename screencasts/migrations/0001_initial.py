# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaScreencast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(help_text='Escolha uma op\xe7\xe3o', max_length=3, verbose_name='Tipo', choices=[(b'TU', 'Tutorial'), (b'CD', 'Codigo'), (b'VI', 'Video'), (b'SL', 'Slide')])),
                ('title', models.CharField(help_text='Escolha um Titulo da media. Exemplo Youtube,Slideshare', max_length=255, verbose_name='Titulo')),
                ('url', models.URLField(help_text='Escolha a Url que esta localizada a media', verbose_name='URL')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Media dos screencasts',
                'verbose_name_plural': 'Medias dos screencasts',
            },
        ),
        migrations.CreateModel(
            name='Screencast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Informe um titulo da palestra', max_length=255, verbose_name='Titulo')),
                ('slug', models.SlugField(null=True, help_text='Informe um slug para o titulo da palestra', unique=True, verbose_name='Slug')),
                ('summary', models.TextField(help_text='Descreva um sum\xe1rio para sua palestra', verbose_name='Sum\xe1rio')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Screencasts',
                'verbose_name_plural': 'Screencasts',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=255, unique=True, null=True, verbose_name='Slug')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AddField(
            model_name='screencast',
            name='serie',
            field=models.ForeignKey(verbose_name='Serie', blank=True, to='screencasts.Serie', null=True),
        ),
        migrations.AddField(
            model_name='screencast',
            name='speaker',
            field=models.ForeignKey(verbose_name='Palestrante', to=settings.AUTH_USER_MODEL, help_text='A quem essa palestra pertence'),
        ),
        migrations.AddField(
            model_name='screencast',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='mediascreencast',
            name='screencast',
            field=models.ForeignKey(related_name='medias', verbose_name='Screencasts', to='screencasts.Screencast'),
        ),
    ]
