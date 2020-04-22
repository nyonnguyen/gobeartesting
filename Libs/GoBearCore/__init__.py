from SeleniumLibrary import SeleniumLibrary
from .keywords import *
import sys

__version__ = '1.0.0'


class GoBearCore(SeleniumLibrary):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        SeleniumLibrary.__init__(self, 30)
        self.add_library_components([BrowserKeywords(self), ElementKeywords(self), GoBearCoreKeywords(self)])
        ####################################################################################
        # Make sure pydevd installed: pip install pydevd
        # AND Uncomment following codes to enable debug mode
        sys.path.append("pydevd-pycharm.egg")
        import pydevd
        pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
        ####################################################################################
