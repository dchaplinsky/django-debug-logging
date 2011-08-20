import logging
import traceback
import sys
from copy import deepcopy, Error

from debug_logging.models import TestRun, DebugLogRecord


class DBHandler(logging.Handler):

    def emit(self, record):
        if type(record.msg) is dict:
            # Pull the project name, hostname, and revision out of the record
            filters = {}
            for field in ('project_name', 'hostname', 'revision'):
                if field in record.msg.keys():
                    filters[field] = record.msg[field]

            # Find the open test run for this project
            try:
                test_run = TestRun.objects.get(end__isnull=True, **filters)
            except TestRun.DoesNotExist:
                # Don't log this request if there isn't an open TestRun
                return
            record.msg['test_run'] = test_run

            filters = {}
            for field in DebugLogRecord._meta.get_all_field_names():
                # TODO: Understand why I can't deep copy the settings
                if field == "settings":
                    try:
                        filters['settings'] = deepcopy(record.msg[field])
                    except Exception as e:
                        filters['settings'] = {'Exception': '%s' % e.message}

                elif field in record.msg.keys():
                    filters[field] = record.msg[field]

            try:
                instance = DebugLogRecord(**filters)
                instance.save()
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_tb(exc_traceback, file=sys.stdout)
