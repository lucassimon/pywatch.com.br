# -*- coding:utf-8 -*-

"""
Starter fabfile for deploying the {{ project_name }} project.

Change all the things marked CHANGEME. Other things can be left at their
defaults if you are happy with the default layout.

1 - Entrar no projeto
2 - Ativar virtualenv
3 - git pull no repositorio
4 - Instalar requirements de producao/staging
5 - Executar as migrates OBS executar migrate do taggit antes
6 - Executar o collect static
6 - restart no supervisor
7 - restart no nginx
"""

from fabric.api import run, env,  cd, task, sudo
from fabric.contrib.files import exists
from fabric.colors import green, red
#from fabric.decorators import runs_once
from fabric.context_managers import shell_env
# CHANGEME

if not hasattr(env, 'server'):
    print(green('Server de Produção'))
    env.server = u'production'
    env.hosts = ['pywatch@107.170.42.37:52022']
    env.project_name = u'pywatch'
    env.shell = u'/bin/zsh -c'
    env.code_dir = u'~/sites/pywatch.com.br'
    env.git_repo = u'git@github.com:lucassimon/pywatch.com.br.git'
    env.settings = u'--settings=pywatch.settings.production'
    env.virtualenv = u'~/venvs/pywatch.com.br/'
    env.python_bin = env.virtualenv + 'bin/python'
    env.pip_bin = env.virtualenv + 'bin/pip'
    env.webserver = u'nginx'
elif env.server == 'staging':
    print(green('Server de Staging'))
    env.server = 'staging'


def print_env_and_user():
    """
    Print the envirioment and user
    """
    print(red("Executing on %s as %s" % (env.host, env.user)))


def django_manage(command='help', virtualenv='pywatch.com.br', settings=env.settings):
    return "/bin/bash -l -c 'source /usr/local/bin/virtualenvwrapper.sh && workon " + virtualenv + " && " + env.python_bin + " " + env.code_dir + "/manage.py " + command + " " + settings + "'"


def git(cmd):
    with cd(env.code_dir):
        run("git %s" % cmd)


def checkout_master():
    git("checkout master")


def pull():
    git("pull --rebase")


def restart():
    sudo("supervisorctl restart pywatch:gunicorn_pywatch_com_br")
    sudo("service %s restart" % env.webserver)


def start():
    sudo("supervisorctl start pywatch:gunicorn_pywatch_com_br")
    sudo("service %s restart" % env.webserver)


def stop():
    sudo("supervisorctl stop pywatch:gunicorn_pywatch_com_br")


def install_requirements():
    with cd(env.code_dir):
        run("%s install -M -r requirements/"+env.server+".txt" % env.pip_bin)


def collectstatic():
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='collectstatic -l --noinput'))


@task
def uname():
    """ Prints information about the host. """
    #print_env_and_user()
    #run("uname -a")
    #checkout_master()
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage())


@task
def deploy():
    """ Deploy the application """
    pull()
