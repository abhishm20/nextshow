
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Production Host
PRODUCTION_HOST_NAME = 'http://v5.posoapp.com'
PRODUCTION_HOST_PORT = '80'
PRODUCTION_HOST = PRODUCTION_HOST_NAME + ':' + PRODUCTION_HOST_PORT

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
            'class': 'logging.FileHandler',
            'filename': 'log/backend.log',
            'formatter': 'verbose'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/debug.log',
            'formatter': 'verbose'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'log/error.log',
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
