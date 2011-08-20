import os.path
import platform
import subprocess
from logging import Handler

from django.conf import settings
from django.utils.importlib import import_module


def get_project_name():
    return settings.SETTINGS_MODULE.split('.')[0]


def get_hostname():
    return platform.node()

def get_class_from_string(import_path):
    if '.' not in import_path:
        raise TypeError(
            "'import_path' argument to 'debug_logging.utils.get_class' must "
            "contain at least one dot."
        )
    module_name, object_name = import_path.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)

def get_handler_instance(handler):
    try:
        if issubclass(handler, Handler):
            return handler()
    except TypeError as e:
        pass
    try:
        if isinstance(handler, str):
            return get_class_from_string(handler)()
    except:
        pass
    try:
        if isinstance(handler, Handler):
            return handler
    except:
        pass




def get_revision():
    vcs = getattr(settings, 'DEBUG_TOOLBAR_CONFIG', {}).get('VCS', None)
    if vcs == 'git':
        module = import_module(settings.SETTINGS_MODULE)
        path = os.path.realpath(os.path.dirname(module.__file__))
        cmd = 'cd %s && git rev-parse --verify --short HEAD' % path
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        proc_stdout, proc_stderr = proc.communicate()
        return proc_stdout
