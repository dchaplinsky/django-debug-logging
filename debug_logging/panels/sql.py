from django.conf import settings
from debug_toolbar.panels.sql import SQLDebugPanel, reformat_sql

# This whole block is to support the workaround below on the __init__ method,
# and can be deleted once #178 on django-debug-toolbar is closed.
try:
    from django.db import connections
except ImportError:
    # Compatibility with Django < 1.2
    from django.db import connection
    connections = {'default': connection}
    connection.alias = 'default'


class SQLLoggingPanel(SQLDebugPanel):
    """Extends the SQL debug panel to enable logging."""
    
    def process_response(self, request, response):
        if getattr(settings, 'DEBUG_LOGGING_CONFIG', {}).get('ENABLED', False):
            # Call the nav_subtitle method so that the query data is captured
            self.nav_subtitle()
            
            for alias, query in self._queries:
                query['alias'] = alias
            
            stats = {}
            
            queries = [q for a, q in self._queries]
            
            if settings.DEBUG_LOGGING_CONFIG.get('SQL_EXTRA', False):
                stats['sql_queries'] = queries
            
            stats['sql_time'] = self._sql_time
            stats['sql_num_queries'] = len(queries)
            request.debug_logging_stats.update(stats)
