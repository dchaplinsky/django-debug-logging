from django.conf import settings

from debug_logging.handlers import DBHandler

DEFAULT_CONFIG = {
    'ENABLED': False,
    'SQL_EXTRA': True,
    'CACHE_EXTRA': True,
    'BLACKLIST': [],
    'HANDLER': DBHandler,
    'CACHE_EXTRA': False,
    'LOGGED_SETTINGS': None,
}

LOGGING_CONFIG  = dict(DEFAULT_CONFIG,
                       **getattr(settings, 'DEBUG_LOGGING_CONFIG', {}))
