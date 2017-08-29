# Client sercet key
CLIENT_SECRET_KEY = '512c6081e28acca197ba6de0c590875f'

# VALIDATION Service
VALIDATION = True

# HTTP loggin service
HTTP_LOGGING_SERVICE = False

# Session service
SESSION_ACTIVE = False

# Push notification service
PUSH_NOTIFICATION_SERVICE = False

# SMS
SMS_SERVICE_ENABLED = False

#
MAIL_SERVICE_ENABLED = False

# GCM SECRET
GCM_NOTIFICATION_SECRET = '0eb9ee78e3d9bb23ffb1a105a4accefe7166af85a171e54c33a9afb3c590f597'

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
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
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
        }
    },
    'loggers': {
        'custom': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console'],
        }
    }
}
