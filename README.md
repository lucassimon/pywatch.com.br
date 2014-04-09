pywatch.com.br
==============


Master
[![Build Status](https://travis-ci.org/lucassimon/pywatch.com.br.png?branch=master)](https://travis-ci.org/lucassimon/pywatch.com.br)

Staging
[![Build Status](https://travis-ci.org/lucassimon/pywatch.com.br.png?branch=staging)](https://travis-ci.org/lucassimon/pywatch.com.br)

Bem vindo a documentação do PyWatch's!
======================================

O PyWatch é um aplicativo que visa reunir as palestras, tutoriais e screencasts espalhados
na internet. O objetivo principal é montar uma biblioteca sobre Django, Python e outros web frameworks.

Futuramente pretende-se utilizar web semântica para relacionar todo o tipo de conteúdo com seus respectivos
autores.

A inspiração surgiu ao ver o projeto emberwatch.com.

[http://pywatch.readthedocs.org/en/latest/](http://pywatch.readthedocs.org/en/latest/)

Contribuindo com o PyWatch
==========================

Como um projeto open source, o PyWatch da as boas vindas aos contribuintes de todas as formas

Exemplos para contribuir inclui:

* Códigos
* Melhorar a documentação
* Reportar bugs

Para contribuir por favor crie um branch como exemplo, dev_lucas e faça os commits nele.

Testes sempre!

Executando um exemplo
=====================

Crie o ambiente virtual.
Pode-se utilizar o virtualenv ou virtualenvwrapper. Fica a sua escolha.


    cd ~/venvs
    virtualenv pywatch
    source pywatch/bin/activate


Baixe e instale o PyWatch.

    git clone git@github.com:lucassimon/pywatch.com.br.git
    cd pywatch.com.br
    pip install -r requirements/dev.txt

Sincronize o banco de dados.

    cd pywatch.com.br
    python manage.py syncdb --settings=pywatch.settings.dev
    python manage.py migrate taggit --settings=pywatch.settings.dev
    python manage.py migrate --all --settings=pywatch.settings.dev


Execute o PyWatch.

    cd pywatch.com.br
    python manage.py runserver --settings=pywatch.settings.dev

Executando os testes
====================

Crie um banco de dados chamado test_pywatch

Sincronize o banco de dados.

    cd pywatch.com.br
    python manage.py syncdb --settings=pywatch.settings.test
    python manage.py migrate taggit --settings=pywatch.settings.test
    python manage.py migrate --all --settings=pywatch.settings.test


Execute o PyWatch.

    cd pywatch.com.br
    python manage.py test --settings=pywatch.settings.test


ROADMAP for 0.1.1
=================

[ ] Melhorar a homepage

[X] Criar a listagem de palestras

[X] Criar a listagem de palestrantes

[X] Criar a detalhes de palestras

[X] Criar a listagem de palestrantes

[X] Criar pesquisa de palestras com django-haystack e whoosh

[ ] Melhorar o layout de listagem de palestras e palestrantes

CHANGELOG
=========

[LEIA AQUI] (https://github.com/lucassimon/pywatch.com.br/blob/master/docs/CHANGELOG.md)
