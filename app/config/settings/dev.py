from .base import *

WSGI_APPLICATION = 'config.wsgi.dev.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'django_extensions'
]