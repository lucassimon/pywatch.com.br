#!/usr/bin/env python
# -*- coding:utf-8 -*-

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Lucas Simon Rodrigues Magalhaes', 'lucassrod@gmail.com'),
)

MANAGERS = ADMINS

LANGUAGES = (
    ('pt-br', u'Portugues'),
    ('en', u'Ingles'),
)

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = PROJECT_DIR.child('media')

MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '9h+av*y^#32q+7e#%s3o2a)r3xs473y97z(%ub6hx13+=x!4gp'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pywatch.urls'

WSGI_APPLICATION = 'pywatch.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

AUTH_USER_MODEL = 'speakers.SpeakerUser'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'core',
    'dashboards',
    'screencasts',
    'speakers',
    'talks',

    'south',
    'django_extensions',
    'rest_framework',
    'haystack',
    'taggit',
    'mptt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
)

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': (
        'rest_framework.serializers.HyperlinkedModelSerializer'
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.OAuth2Authentication',
        #'rest_framework.authentication.SessionAuthentication',
    ),

}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': PROJECT_DIR + '/whoosh_index',
    },
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # Required by allauth template tags
    'django.core.context_processors.request',
    # allauth specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/dashboard/'

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
