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

            fields = {}
            for field in DebugLogRecord._meta.get_all_field_names():
                if field in record.msg.keys():
                    fields[field] = record.msg[field]

            instance = DebugLogRecord(**fields)
            instance.save()
