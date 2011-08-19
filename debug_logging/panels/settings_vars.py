import re
from django.views.debug import get_safe_settings
from debug_toolbar.panels.settings_vars import SettingsVarsDebugPanel
from debug_logging.settings import LOGGING_CONFIG

DEFAULT_LOGGED_SETTINGS = [
    'CACHE_BACKEND', 'CACHE_MIDDLEWARE_KEY_PREFIX', 'CACHE_MIDDLEWARE_SECONDS',
    'DATABASES', 'DEBUG', 'DEBUG_LOGGING_CONFIG', 'DEBUG_TOOLBAR_CONFIG',
    'DEBUG_TOOLBAR_PANELS', 'INSTALLED_APPS', 'INTERNAL_IPS',
    'MIDDLEWARE_CLASSES', 'TEMPLATE_CONTEXT_PROCESSORS', 'TEMPLATE_DEBUG',
    'USE_I18N', 'USE_L10N'
]


class SettingsVarsLoggingPanel(SettingsVarsDebugPanel):
    """Extends the Settings debug panel to enable logging."""

    def __init__(self, *args, **kwargs):
        super(SettingsVarsLoggingPanel, self).__init__(*args, **kwargs)
        self.logged_settings = LOGGING_CONFIG['LOGGED_SETTINGS']
        if not self.logged_settings:
            self.logged_settings = DEFAULT_LOGGED_SETTINGS
        self.logged_settings_re = re.compile('|'.join(self.logged_settings))

    def process_response(self, request, response):
        if LOGGING_CONFIG['ENABLED']:
            # Logging is enabled, so log the settings
            safe_settings = get_safe_settings()
            log_settings = {}
            for k, v in safe_settings.items():
                if self.logged_settings_re.search(k):
                    log_settings[k] = v

            request.debug_logging_stats['settings'] = log_settings
