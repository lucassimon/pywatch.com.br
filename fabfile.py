# -*- coding:utf-8 -*-

"""
Starter fabfile for deploying the {{ project_name }} project.

Change all the things marked CHANGEME. Other things can be left at their
defaults if you are happy with the default layout.

"""

from fabric.api import run, env,  cd, task, sudo
from fabric.colors import green, red
# from fabric.decorators import runs_once
from fabric.context_managers import shell_env
# CHANGEME
# Usar fab <command> --set server=prod para executar em producao

if not hasattr(env, 'server'):
    print(green('Server de Produção'))
    env.server = 'production'
    env.hosts = ['pywatch@107.170.42.37:52022']
    env.project_name = u'pywatch'
    env.shell = u'/bin/zsh -c'
    env.code_dir = u'~/sites/pywatch.com.br'
    env.git_repo = u'git@github.com:lucassimon/pywatch.com.br.git'
    env.settings = u'--settings=pywatch.settings.production'
    env.virtualenv_name = 'pywatch.com.br'
    env.virtualenv = '~/venvs/pywatch.com.br/'
    env.python_bin = env.virtualenv + 'bin/python'
    env.pip_bin = env.virtualenv + 'bin/pip'
    env.webserver = u'nginx'
elif env.server == 'staging':
    print(green('Server de Staging'))
    env.server = 'staging'
    env.hosts = ['pywatch@192.81.211.65']
    env.project_name = u'pywatch'
    env.shell = u'/bin/zsh -c'
    env.code_dir = u'~/sites/staging-pywatch'
    env.git_repo = u'git@github.com:lucassimon/pywatch.com.br.git'
    env.settings = u'--settings=pywatch.settings.staging'
    env.virtualenv_name = 'staging-pywatch'
    env.virtualenv = '~/venvs/staging-pywatch/'
    env.python_bin = env.virtualenv + 'bin/python'
    env.pip_bin = env.virtualenv + 'bin/pip'
    env.webserver = u'nginx'


def print_env_and_user():
    """
    Print the envirioment and user
    """
    print(red("Executing on %s as %s" % (env.host, env.user)))


def django_manage(command='help', virtualenv=env.virtualenv_name, settings=env.settings):
    """
    Returns a absolute path to execute manage.py
    """
    return "/bin/bash -l -c 'source /usr/local/bin/virtualenvwrapper.sh && workon " + virtualenv + " && " + env.python_bin + " " + env.code_dir + "/manage.py " + command + " " + settings + "'"


def git(cmd):
    """
    Create a method to execute git on the server
    """
    with cd(env.code_dir):
        run("git %s" % cmd)


def checkout_master():
    """
    Run git checkout master command on repository
    """
    git("checkout master")


def pull():
    """
    Run git pull command on repository
    """
    git("pull --rebase")


def restart():
    """
    Restart supervisor and webserver
    """
    sudo("supervisorctl restart pywatch:%s_pywatch_com_br" % (env.server))
    sudo("service %s restart" % env.webserver)


def start():
    """
    Start supervisor and webserver
    """
    sudo("supervisorctl restart pywatch:%s_pywatch_com_br" % (env.server))
    sudo("service %s restart" % env.webserver)


def stop():
    """
    Stopping supervisor
    """
    sudo("supervisorctl restart pywatch:%s_pywatch_com_br" % (env.server))


def install_requirements():
    """
    Install all requirements by the server
    """
    with cd(env.code_dir):
        run(
            "%s install -r %s/requirements/%s.txt"
            % (
                env.pip_bin,
                env.code_dir,
                env.server
            )
        )


def collectstatic():
    """
    Collect the static files
    """
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='collectstatic -l --noinput'))


@task
def uname():
    """ Prints information about the host. """
    print_env_and_user()
    run("uname -a")


@task
def deploy():
    """ Deploy the application """
    print_env_and_user()
    pull()
    install_requirements()
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='syncdb --noinput'))
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='migrate taggit'))
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='migrate --all'))
    collectstatic()
    restart()


@task
def haystack_update_index():
    """Haystack command to update indexes"""
    print_env_and_user()
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='update_index'))


@task
def haystack_rebuild_index():
    """Haystack command to rebuild indexes"""
    print_env_and_user()
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command='rebuild_index'))


@task
def run_manage():
    """ Run manage.py with command line """
    print_env_and_user()
    command_line = raw_input('Digite o comando para o manage.py \n Ex: help, migrate, dbshell\n> ')
    with shell_env(WORKON_HOME='~/venvs'):
        run(django_manage(command=command_line))
