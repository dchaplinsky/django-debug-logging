from logging import StreamHandler, Formatter

from django.conf import settings

from debug_logging.utils import get_handler_instance

fmt_tick = Formatter('-')
sth_ticker = StreamHandler()
sth_ticker.setFormatter(fmt_tick)

DEFAULT_LOGGED_SETTINGS = [
    'CACHE_BACKEND', 'CACHE_MIDDLEWARE_KEY_PREFIX', 'CACHE_MIDDLEWARE_SECONDS',
    'DATABASES', 'DEBUG', 'DEBUG_LOGGING_CONFIG', 'DEBUG_TOOLBAR_CONFIG',
    'DEBUG_TOOLBAR_PANELS', 'INSTALLED_APPS', 'INTERNAL_IPS',
    'MIDDLEWARE_CLASSES', 'TEMPLATE_CONTEXT_PROCESSORS', 'TEMPLATE_DEBUG',
    'USE_I18N', 'USE_L10N'
]

DEFAULT_CONFIG = {
    'SQL_EXTRA': False,
    'CACHE_EXTRA': False,
    'BLACKLIST': [],
    'LOGGING_HANDLERS': (sth_ticker, 'debug_logging.handlers.DBHandler'),
    'LOGGED_SETTINGS': None,
    'LOGGED_SETTINGS': [
    'CACHE_BACKEND', 'CACHE_MIDDLEWARE_KEY_PREFIX', 'CACHE_MIDDLEWARE_SECONDS',
    'DATABASES', 'DEBUG', 'DEBUG_LOGGING_CONFIG', 'DEBUG_TOOLBAR_CONFIG',
    'DEBUG_TOOLBAR_PANELS', 'INSTALLED_APPS', 'INTERNAL_IPS',
    'MIDDLEWARE_CLASSES', 'TEMPLATE_CONTEXT_PROCESSORS', 'TEMPLATE_DEBUG',
    'USE_I18N', 'USE_L10N'],
}

def get_logging_config():
    _logging_config = dict(DEFAULT_CONFIG,
                          **getattr(settings, 'DEBUG_LOGGING_CONFIG', {}))

    _logging_config['LOGGING_HANDLERS'] = [get_handler_instance(handler)
                                                for handler in _logging_config['LOGGING_HANDLERS']]
    return _logging_config


LOGGING_CONFIG  = get_logging_config()
