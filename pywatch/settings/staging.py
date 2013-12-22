import os
from base import *
from decouple import ConfigIni
import dj_database_url


config = ConfigIni(PROJECT_DIR.child('confs')+'/settings.ini')
########## INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'django_nose',
    'nose',
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
        default=config('DATABASE_TEST_URL')
    )
}
########## END DATABASE CONFIGURATION
