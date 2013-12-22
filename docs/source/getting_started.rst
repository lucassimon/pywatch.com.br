Começando
=========

Buscando ajuda
--------------

Se você tiver problemas e não consegue descobrir como resolve-lo, você pode obter ajuda a partir de
nosso sistema de tickets.


Configurando o ambiente.
------------------------

Instalando os pacotes necessarios. ::

    $ sudo aptitude install build-essential libpq-dev git git-core python-dev python-virtualenv python-pip libcurl4-gnutls-dev

Configurando o virtualenv ou virtualenvwrapper.
-----------------------------------------------

VirtualEnv. ::

    $ mkdir ~/venvs
    $ cd ~/venvs
    $ virtualenv --unzip-setuptools pywatch
    $ source ~/venvs/pywatch/bin/activate

Virtualenvwrapper. ::

    $ mkdir ~/venvs
    $ sudo pip install virtualenvwrapper
    $ echo >> "source '/usr/local/bin/virtualenvwrapper.sh'" .bashrc/.zshrc
    $ echo >> "WORKON_HOME='~/venvs'
    $ mkvirtualenv pywatch

Ativar o ambiente. ::

    $ workon pywatch

Clonando o repositorio do projeto
---------------------------------

Definir uma pasta para conter os projetos:
code, workspace-django, projetos etc... ::

    $ mkdir ~/workspace-django
    $ cd ~/workspace-django
    $ git clone git@github.com:lucassimon/pywatch.com.br.git
    $ cd pywatch.com.br

Instalando os pacotes do requirements.txt
-----------------------------------------


Pacotes de desenvolvimento. ::

    $ cd workspace-django/pywatch.com.br
    $ pip install -r requirements/dev.txt


Executar o syncdb e fazer as migrações
--------------------------------------

Primeiro o syncdb. ::

    $ cd pywatch.com.br
    $ python manage.py syncdb --migrate --settings=pywatch.settings.dev

Segundo, executar as migrates. ::

    $ python manage.py migrate --all --settings=pywatch.settings.dev

Executar o runserver
--------------------

Execute. ::

    $ cd pywatch.com.br
    $ python manage.py runserver --settings=pywatch.settings.dev
