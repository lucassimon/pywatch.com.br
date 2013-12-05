Bem vindo a documentação do PyWatch's!
======================================

O PyWatch é um aplicativo que visa reunir as palestras, tutoriais e screencasts espalhados
na internet. O objetivo principal é montar uma biblioteca sobre Django, Python e outros web frameworks.

Futuramente pretende-se utilizar web semântica para relacionar todo o tipo de conteúdo com seus respectivos
autores.

A inspiração surgiu ao ver o projeto emberwatch.com.

Contribuindo com o PyWatch
==========================

Como um projeto open source, o PyWatch da as boas vindas aos contribuintes de todas as formas

Exemplos para contribuir inclui:

* Códigos
* Melhorar a documentação
* Reportar bugs

Executando um exemplo
=====================

Crie o ambiente virtual.
Pode-se utilizar o virtualenv ou virtualenvwrapper. Fica a sua escolha.

.. code-block::
    cd ~/venvs
    virtualenv pywatch
    source pywatch/bin/activate


Baixe e instale o PyWatch

    git clone git@github.com:lucassimon/pywatch.com.br.git
    cd pywatch.com.br
    pip install -r pywatch/requirements/dev.txt

Sincronize o banco de dados

    cd pywatch.com.br
    python manage.py syncdb --migrate --settings=pywatch.settings.dev


Execute o PyWatch

    cd pywatch.com.br
    python manage.py runserver --settings=pywatch.settings.dev



Contents:

.. toctree::
   :maxdepth: 2
   how_to_use
   how_to_contribute
   faq
   license
   contact



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

