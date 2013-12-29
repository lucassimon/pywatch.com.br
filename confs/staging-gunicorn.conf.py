import os

bind = "127.0.0.1:9002"
workers = (os.sysconf("SC_NPROCESSORS_ONLN") * 2) + 1
loglevel = "error"
pidfile = "/home/pywatch/run/staging-pywatch-site.pid"
accesslog = "/home/pywatch/logs/gunicorn/gunicorn-access-staging-pywatch-site.log"
errorlog = "/home/pywatch/logs/gunicorn/gunicorn-error-staging-pywatch-site.log"
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'http',
                         'X-FORWARDED-PROTO': 'http',
                         'X-FORWARDED-SSL': 'off'}
