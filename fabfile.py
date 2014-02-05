# -*- coding:utf-8 -*-

"""
Starter fabfile for deploying the {{ project_name }} project.

Change all the things marked CHANGEME. Other things can be left at their
defaults if you are happy with the default layout.
"""

import posixpath

from fabric.api import run, local, env, settings, cd, task, sudo
from fabric.contrib.files import exists
from fabric.operations import _prefix_commands, _prefix_env_vars
from fabric.colors import green, red
#from fabric.decorators import runs_once
#from fabric.context_managers import cd, lcd, settings, hide

# CHANGEME
env.hosts = ['pywatch@192.81.211.65']
env.project_name = 'pywatch'
#env.shell = '/bin/zsh -c'
#env.code_dir = '/srv/www/{{ project_name }}'
#env.project_dir = '/srv/www/{{ project_name }}/{{ project_name }}'
#env.static_root = '/srv/www/{{ project_name }}/static/'
#env.virtualenv = '/srv/www/{{ project_name }}/.virtualenv'
env.git_repo = 'git@github.com:lucassimon/pywatch.com.br.git'
#env.django_settings_module = '{{ project_name }}.settings'

# Python version
PYTHON_BIN = "python2.7"
PYTHON_PREFIX = ""  # e.g. /usr/local  Use "" for automatic
PYTHON_FULL_PATH = "%s/bin/%s" % (PYTHON_PREFIX, PYTHON_BIN) if PYTHON_PREFIX else PYTHON_BIN

# Set to true if you can restart your webserver (via wsgi.py), false to stop/start your webserver
# CHANGEME
DJANGO_SERVER_RESTART = False


@task
def uname():
    """ Prints information about the host. """
    run("uname -a")


@task
def first_deployment_mode():
    """
    Use before first deployment to switch on fake south migrations.
    """
    env.initial_deploy = True
    print(green("Primeiro deploy......."))

    run_aptitude_update_and_upgrade()

    install_initial_packages()

    setup_git()

    boost_power_vim()

    #boost_power_shell_zsh()

    install_pip_packages()

    create_directories()

    print(red('Insira a chave publica gerada em .ssh/id_rsa.pub no github'))
    input('Pressione uma tecla para continuar')

    #create_staging()


@task
def run_aptitude_update_and_upgrade():
    """
    Run aptitude update and aptitude upgrade
    """
    print(green("Atualizando a lista de pacotes"))
    sudo('aptitude update')

    print(green("Atualizando pacotes do sistema"))
    sudo('aptitude safe-upgrade -y')


@task
def install_initial_packages():
    """
    Install the core packages of the system
    """
    run_aptitude_update_and_upgrade()
    print(green("Instala pacotes do ambiente django"))
    sudo('aptitude install build-essential libpq-dev git git-core python-dev \
python-setuptools python-virtualenv python-psycopg2 python-pip \
python-software-properties vim zsh ntp ntpdate openssl xclip \
exuberant-ctags vim-gnome nginx supervisor -y')


@task
def install_pip_packages():
    """
    Install flake8 and virtualenvwrapper
    """
    print(green("Instalando o flake8 e virtualenvwrapper"))
    sudo('pip install flake8 virtualenvwrapper')
    run("echo 'source /usr/local/bin/virtualenvwrapper.sh' >> .zshrc ")
    run("echo 'export WORKON_HOME=$HOME/venvs' >> .zshrc ")
    run("source .zshrc ")


@task
def setup_git():
    """
    Setup and generate ssh-keygen
    """
    print(green('Baixando o arquivo .gitconfig'))
    run('wget --no-check-certificate https://gist.github.com/lucassimon/6224006/raw/175ac76748c067ed92a89d5add3e23dccda85cae/.gitconfig')
    run('ssh-keygen -t rsa -C "lucassrod@gmail.com"')


@task
def boost_power_vim():
    """
    Boost power of vim
    """
    print(green("Bombando o vim"))
    run('curl https://raw.github.com/lerrua/vimfiles/master/bootstrap.sh -o- | sh')


@task
def upgrade_bundle_vim():
    """
    Upgrade packages of vim
    """
    print(green("Atualizando os pacotes do Bundle"))
    with cd('$HOME/.vim/'):
        run('git pull')
        run('vim +BundleUpdate +qall')
        run('pwd')

    with cd('$HOME'):
        print(green("Atualizado"))


@task
def boost_power_shell_zsh():
    """
    Boost power of shell
    """
    print(green("Bombando o shell"))
    run('curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh')
    sudo('chsh -s /bin/zsh')


@task
def create_directories():
    """
    Create directories
    """
    print(green("Criando os diretorios"))
    run('mkdir run venvs sites')
    run('mkdir -p logs/{gunicorn,nginx,supervisor}')
    sudo('chgrp www-data logs/nginx')
    sudo('chmod -R 775 logs/nginx')


@task
def create_staging():
    """
    Create staging app
    """
    print(green("Criando ambiente virtual staging"))
    run('export WORKON_HOME=$HOME/venvs')
    run('source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv --system-site-packages staging-%s' % env.project_name)
    with cd('$HOME/sites'):
        run('git clone %s staging-%s' % (env.git_repo, env.project_name))

    with cd('$HOME/sites/staging-%s' % (env.project_name)):
        run('git checkout -b staging origin/staging')
        install_dependencies('staging')


@task
def install_dependencies(branch=None):
    """
    Install dependencies by branch
    """
    with cd('$HOME'):
        print(green("Instalando as dependencias"))
    print(branch)
    print(type(branch))
    print(branch == 'staging')
    if branch is None:
        return 0
    elif branch == 'staging':
        print('bucetaaaaaa')
        run('export WORKON_HOME=$HOME/venvs')
        run('source /usr/local/bin/virtualenvwrapper.sh && workon staging-%s' % env.project_name)
        with cd('$HOME/sites/staging-%s' % (env.project_name)):
            run('pip install -r requirements/dev.txt --upgrade')
    elif branch is 'master':
        run('export WORKON_HOME=$HOME/venvs')
        run('source /usr/local/bin/virtualenvwrapper.sh && workon staging-%s' % env.project_name)
        with cd('$HOME/sites/%s' % (env.project_name)):
            run('pip install -r requirements/production.txt --upgrade')
    else:
        return 0
