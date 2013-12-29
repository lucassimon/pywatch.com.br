import os
from base import *
from decouple import ConfigIni
import dj_database_url


########## DEBUG CONFIGURATION
DEBUG = True

TEMPLATE_DEBUG = DEBUG

########## END DEBUG CONFIGURATION

config = ConfigIni(PROJECT_DIR.child('confs')+'/settings.ini')
########## INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'django_nose',
    'nose',
    'gunicorn',
)

########## TEST SETTINGS
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
TEST_DISCOVER_ROOT = PROJECT_DIR
TEST_DISCOVER_PATTERN = "test_*"
NOSE_ARGS = ['--verbosity=2', '-x', '-d']
os.environ['REUSE_DB'] = "1"
########## END TEST SETTINGS

########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_STAGING_URL')
    )
}
########## END DATABASE CONFIGURATION

##########  MAILTRAP CONFIGURATION

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

##########  END MAILTRAP CONFIGURATION

ALLOWED_HOSTS = ['staging-pywatch.lucassimon.com.br', '*.staging-pywatch.lucassimon.com.br', '192.81.211.65']
