from base import *


########## INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'django_nose',
)

########## TEST SETTINGS
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
TEST_DISCOVER_ROOT = PROJECT_DIR
TEST_DISCOVER_PATTERN = "test_*"
########## END TEST SETTINGS

########## DEBUG CONFIGURATION
DEBUG = True

TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = not DEBUG
########## END DEBUG CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_TEST_URL')
    )
}
########## END DATABASE CONFIGURATION
