

class NullBackend(object):

    def __init__(self, number_of_failed_tests, *args, **kwargs):
        self._number_of_failed_tests = number_of_failed_tests

    def aftermath(self):
        pass
