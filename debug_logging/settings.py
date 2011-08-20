from django.conf import settings

from debug_logging.utils import get_class_from_string

DEFAULT_CONFIG = {
    'ENABLED': False,
    'SQL_EXTRA': True,
    'CACHE_EXTRA': True,
    'BLACKLIST': [],
    'LOGGING_HANDLERS': ('debug_logging.handlers.DBHandler',),
    'CACHE_EXTRA': False,
    'LOGGED_SETTINGS': None,
}

def get_logging_config():
    _logging_config = dict(DEFAULT_CONFIG,
                          **getattr(settings, 'DEBUG_LOGGING_CONFIG', {}))

    _logging_config['LOGGING_HANDLERS'] = [get_class_from_string(klass_string)
                                                for klass_string in _logging_config['LOGGING_HANDLERS']]
    return _logging_config


LOGGING_CONFIG  = get_logging_config()
