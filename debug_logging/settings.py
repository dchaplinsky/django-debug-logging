from django.conf import settings

from debug_logging.utils import get_handler_instance

DEFAULT_CONFIG = {
    'ENABLED': False,
    'SQL_EXTRA': False,
    'CACHE_EXTRA': False,
    'BLACKLIST': [],
    'LOGGING_HANDLERS': ('debug_logging.handlers.DBHandler',),
    'LOGGED_SETTINGS': None,
}

def get_logging_config():
    _logging_config = dict(DEFAULT_CONFIG,
                          **getattr(settings, 'DEBUG_LOGGING_CONFIG', {}))

    _logging_config['LOGGING_HANDLERS'] = [get_handler_instance(handler)
                                                for handler in _logging_config['LOGGING_HANDLERS']]
    return _logging_config


LOGGING_CONFIG  = get_logging_config()
