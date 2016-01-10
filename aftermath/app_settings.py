import django
from django.conf import settings

if django.VERSION[:2] < (1, 9):
    from django.utils import importlib
else:
    import importlib


# Taken from django-rest-framework
def import_from_string(val):
    """
    Attempt to import a class from a string representation.
    """
    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '{0}'".format(val)
        raise ImportError(msg)


AFTERMATH_RUN_ON_FAIL = getattr(settings, 'AFTERMATH_RUN_ON_FAIL', True)
AFTERMATH_RUN_ON_SUCCESS = getattr(settings, 'AFTERMATH_RUN_ON_SUCCESS', True)
AFTERMATH_BACKEND = getattr(settings, 'AFTERMATH_BACKEND', 'aftermath.backends.NullBackend')
AFTERMATH_BACKEND_CLASS = import_from_string(AFTERMATH_BACKEND)
