import os
import json
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

SECRET_ROOT = os.path.join(ROOT_DIR, '.secrets_key')
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

secrets = json.load(open(os.path.join(SECRET_ROOT, 'secrets.json')))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets['SECRET_KEY']

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Add Module
    'doll.apps.DollConfig',
    'equip.apps.EquipConfig',

    # test Module
    'members.apps.MembersConfig',
    # 'tactical_dolls',
    # 'tactical_fairys',
    # 'tactical_equips',

    # Base Module
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django REST
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',

    # Sentry
    'raven.contrib.django.raven_compat',
]

# Sentry Setting
# Error massage by 'dev.younlab@gmail.com'
RAVEN_CONFIG = {
    'dsn': secrets['SENTRY_DSN'],
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # ),
}

ROOT_URLCONF = 'config.urls'

AUTH_USER_MODEL = 'members.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
