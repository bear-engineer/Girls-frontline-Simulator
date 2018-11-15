from .base import *

WSGI_APPLICATION = 'config.wsgi.dev.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    # debug_toolbar
    'debug_toolbar',
    'django_extensions',
    'corsheaders',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets['DEV_DB_NAME'],
        'USER': secrets['DEV_DB_USER'],
        'PASSWORD': secrets['DEV_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    'localhost:8080',
)
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.'

# debug toolbar setting
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE += [
    # debug toolbar
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
