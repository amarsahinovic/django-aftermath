from django.core.exceptions import ImproperlyConfigured
from .app_settings import (
    AFTERMATH_RUN_ON_FAIL, AFTERMATH_RUN_ON_SUCCESS,
    AFTERMATH_BACKEND_CLASS
)

# TODO: For django 1.6, use default test runner, and leave this check for 1.5
try:
    from discover_runner import DiscoverRunner
except ImportError:
    raise ImproperlyConfigured("Please make sure you have "
                               "django-discover-runner installed.")

# Looks nicer to instantiate normally capitalized class :)
Backend = AFTERMATH_BACKEND_CLASS


class AftermathTestRunner(DiscoverRunner):

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        result = super(AftermathTestRunner, self).run_tests(test_labels,
                                                            extra_tests,
                                                            **kwargs)
        if result == 0 and AFTERMATH_RUN_ON_SUCCESS:
            b = Backend(result)
            b.aftermath()
        elif result > 0 and AFTERMATH_RUN_ON_FAIL:
            b = Backend(result)
            b.aftermath()
        return result
