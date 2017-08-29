# Client sercet key
CLIENT_SECRET_KEY = '512c6081e28acca197ba6de0c590875f'

# VALIDATION Service
VALIDATION = True

# HTTP loggin service
HTTP_LOGGING_SERVICE = True

# Session service
SESSION_ACTIVE = True

# Push notification service
PUSH_NOTIFICATION_SERVICE = True

# SMS
SMS_SERVICE_ENABLED = True

#
MAIL_SERVICE_ENABLED = True

# GCM SECRET
GCM_NOTIFICATION_SECRET = '0eb9ee78e3d9bb23ffb1a105a4accefe7166af85a171e54c33a9afb3c590f597'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Production Host
PRODUCTION_HOST_NAME = 'http://v5.posoapp.com'
PRODUCTION_HOST_PORT = '80'
PRODUCTION_HOST = PRODUCTION_HOST_NAME + ':' + PRODUCTION_HOST_PORT

# Celery setup
BROKER_URL = "amqp://ubuntu:ainaa@localhost:5672/mojohost"

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
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'db': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'backupCount': '30',
            'filename': 'log/db.log',
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
        'warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'log/warning.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['db'],
        },
        'django': {
            'handlers': ['warning', 'error'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['warning', 'error'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'custom': {
            'handlers': ['debug', 'error'],
            'level': 'DEBUG'
        }
    }
}
