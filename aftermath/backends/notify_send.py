import os


class NotifySendBackend(object):

    def __init__(self, number_of_failed_tests, *args, **kwargs):
        self._number_of_failed_tests = number_of_failed_tests
        self._success_command = "notify-send --icon='gtk-apply' 'All tests finished successfully'"
        self._fail_command = "notify-send --icon='dialog-error' 'Tests failed' '{0} tests failed.'".format(number_of_failed_tests)

    def aftermath(self):
        command = self._success_command
        if self._number_of_failed_tests > 0:
            command = self._fail_command
        try:                                                                    
            os.popen(command)                                                       
        except Exception, e:                                                    
            print e.message                                                     
