from .base import *
from decouple import Config
import dj_database_url


config = Config(PROJECT_DIR.child('confs')+'/settings.ini')

##########  MAILTRAP CONFIGURATION

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

##########  END MAILTRAP CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
########## END DATABASE CONFIGURATION

INSTALLED_APPS += (
    'gunicorn',
)

##########  AMAZON S3 CONFIGURATION

# 1 - Create the variables envoirement
# AWS_STORAGE_BUCKET_NAME='test'
# 2 - Export the varables
# export AWS_STORAGE_BUCKET_NAME
# 3 - Get the secret and access key in
# https://console.aws.amazon.com/iam/home?#security_credential

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_IS_GZIPPED = True
    AWS_QUERYSTRING_EXPIRE = 7200
    AWS_S3_SECURE_URLS = True
    STATIC_URL = S3_URL
########## END AMAZON S3 CONFIGURATION


##########  COMPRESS CONFIGURATION
if not DEBUG:
    COMPRESS_ENABLED = not DEBUG
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    COMPRESS_CSSTIDY_ARGUMENTS = '--template=highest --sort_properties=false --sort_selectors=false --merge_selectors=1'
    COMPRESS_URL = S3_URL
    COMPRESS_PRECOMPILERS = (
        ('text/coffeescript', 'coffee --compile --stdio'),
        ('text/less', 'lessc {infile} > {outfile}')
    )

##########  COMPRESS CONFIGURATION

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = '*'
