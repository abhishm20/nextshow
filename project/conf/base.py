import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(
    os.path.join(BASE_DIR, 'apps')
)
sys.path.append(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-upy11xi-87ewv)s8#7lsw%t@v!d!ocq4yt)olklx0bn%ti@fc'

ALLOWED_HOSTS = ['*']

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',

    'django_s3_storage',
    'rest_framework',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

from pprint import pprint

pprint(sys.path)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(BASE_DIR, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nextshow',
        'USER': 'root',
        'PASSWORD': 'ainaa',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8',
            'init_command': 'SET '
                            'character_set_connection=utf8,'
                            'collation_connection=utf8_bin'
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'TIMEOUT': 5,
        'VERSION': 1,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    }
}
CACHE_EXPIRY = 60*60*24*30

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'media'))

# RESOURCES CONFIGURATION
RESOURCE_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'project', 'resources'))

TEMP_DIR = os.path.normpath(os.path.join(MEDIA_ROOT, 'temp'))


# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
# STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


