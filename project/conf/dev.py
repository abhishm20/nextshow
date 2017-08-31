
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Production Host
PRODUCTION_HOST_NAME = 'http://192.168.0.102'
PRODUCTION_HOST_PORT = '8000'
PRODUCTION_HOST = PRODUCTION_HOST_NAME + ':' + PRODUCTION_HOST_PORT

# Celery setup
BROKER_URL = "amqp://abhishek:ainaa@localhost:5672/myhost"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s %(funcName)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['app'],
            'level': 'DEBUG'
        },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG'
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR'
        }
    }
}
