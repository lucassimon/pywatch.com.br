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
    $ virtualenv --unzip-setuptools [nomedoprojeto]
    $ source ~/venvs/[nomedoprojeto]/bin/activate

Virtualenvwrapper. ::
    $ mkdir ~/venvs
    $ sudo pip install virtualenvwrapper
    $ echo >> "source '/usr/local/bin/virtualenvwrapper.sh'" .bashrc/.zshrc
    $ echo >> "WORKON_HOME='~/venvs'
    $ mkvirtualenv [nomedoprojeto]

Ativar o ambiente. ::
    $ workon [nomedoprojeto]

Clonando o repositorio do projeto
---------------------------------

Definir uma pasta para conter os projetos:
code, workspace-django, projetos etc... ::

    $ mkdir ~/Code
    $ cd ~/Code
    $ git clone git@github.com:intip/portal-casablanca.git
    $ cd ~/Code/portal-casablanca/cblanca

Configurando o projeto
----------------------

Inicializar os submodulos. ::

    $ cd ~/code/portal-casablanca/
    $ git submodule init
    $ git submodule update


Instalando os pacotes do requirements.txt
-----------------------------------------


Pacotes do WebServices. ::
    $ cd ~/Code/portal-casablanca/cblanca/webservices
    $ pip install -r requirements.txt


Executar o syncdb e fazer as migrações
--------------------------------------

Primeiro o syncdb. ::

    $ cd ~/code/portal-casablanca/cblanca
    $ python manage.py syncdb

LER ATENTAMENTE O QUE ESTA SENDO PEDIDO

egundo, executar as migrates. ::

    $ python manage.py migrate --all

LER ATENTAMENTE O QUE ESTA SENDO PEDIDO. SE GERAR ERRO FAZER AS MIGRACOES UMA A UMA.



Executar o runserver
--------------------

Execute.::

    $ cd ~/code/portal-casablanca/cblanca
    $ python manage.py runserver

